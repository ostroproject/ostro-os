#!/usr/bin/env python


# Copyright (C) 2015 Intel Corporation
#
# Released under the MIT license (see COPYING.MIT)
# ./runtest.py -b build_data.json -a tag -f test.manifest

import sys
import os
import time
import unittest
import inspect
from optparse import OptionParser
from oeqa.oetest import oeTest
from oeqa.oetest import oeRuntimeTest
from oeqa.oetest import runTests
from oeqa.runexported import FakeTarget
from oeqa.runexported import MyDataDict
from oeqa.runexported import TestContext
from oeqa.utils.sshcontrol import SSHControl

try:
    import simplejson as json
except ImportError:
    import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "oeqa")))

def _check(obj, taglist):
    """ match tag inside obj """
    for tag in taglist:
        tkeyval = tag.split("=")
        tkey = tkeyval[0]
        if hasattr(obj, tkey):
            tval = True if len(tkeyval) == 1 else tkeyval[1]
            if tval == getattr(obj, tkey):
                return True
    return False

def check_tag_method(tcase, taglist):
    """ check if test method has specified tag enabled """
    if not hasattr(tcase, "_testMethodName"):
        return False
    tc_method = getattr(tcase, tcase._testMethodName)
    return _check(tc_method, taglist)

def check_tag_class(tcase, taglist):
    """ check if test class has specified tag enabled """
    if not hasattr(tcase, "_testMethodName"):
        return False
    tc_method = getattr(tcase, tcase._testMethodName)
    tc_class = tc_method.__self__.__class__
    return _check(tc_class, taglist)

def runTests_tag(tc, taglist):
    """ run whole test suite according to tclist"""
    # set the context object passed from the test class
    setattr(oeTest, "tc", tc)
    # set ps command to use
    setattr(oeRuntimeTest, "pscmd", "ps -ef" if oeTest.hasPackage("procps") else "ps")
    # prepare test suite, loader and runner
    suite = unittest.TestSuite()
    testloader = unittest.TestLoader()
    testloader.sortTestMethodsUsing = None
    for tname in tc.testslist:
        tsuite = testloader.loadTestsFromName(tname)
        for ts in tsuite:
            # it is test suite
            if hasattr(ts, "_tests") and ts._tests != []:
                if check_tag_class(ts._tests[0], taglist):
                    print "add suite"
                    suite.addTest(ts)
                else:
                    for x in ts._tests:
                        if check_tag_class(x, taglist) or\
                               check_tag_method(x, taglist):
                            suite.addTest(x)
            # it is test case
            else:
                if check_tag_class(ts, taglist) or\
                       check_tag_method(ts, taglist):
                    suite.addTest(ts)
    print("Test modules  %s" % tc.testslist)
    print("Found %s tests" % suite.countTestCases())
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result

def main():

    usage = "usage: %prog [options]"
    parser = OptionParser(usage=usage)
    parser.add_option("-t", "--target-ip", dest="ip",
            help="The IP address of the target machine. Use this to \
            overwrite the value determined from TEST_TARGET_IP at build time")
    parser.add_option("-s", "--server-ip", dest="server_ip",
            help="The IP address of this machine. Use this to \
            overwrite the value determined from TEST_SERVER_IP at build time.")
    parser.add_option("-d", "--deploy-dir", dest="deploy_dir",
            help="Full path to the package feeds, that this \
            the contents of what used to be DEPLOY_DIR on the build machine. \
            If not specified it will use the value specified in the json if \
            that directory actually exists or it will error out.")
    parser.add_option("-l", "--log-dir", dest="log_dir",
            help="This sets the path for TEST_LOG_DIR. If not specified \
            the current dir is used. This is used for usually creating a \
            ssh log file and a scp test file.")
    parser.add_option("-f", "--test-manifest", dest="tests_list",
            help="The test list file")
    parser.add_option("-b", "--build-data", dest="build_data",
            help="The build data file.")
    parser.add_option("-a", "--tag", dest="tag",
            help="The tags to filter test case")
    parser.add_option("-r", "--pkgarch", dest="pkgarch",
            help="The package arch")
    parser.add_option("-n", "--nativearch", dest="nativearch",
            help="The native arch")


    (options, args) = parser.parse_args()

    tc = TestContext()

    #inject testcase list
    tclist = []
    for each_manifest in options.tests_list.split():
        with open(each_manifest, "r") as f:
            map(lambda y:tclist.append(y) if y not in tclist else None, 
                filter(lambda x: not x.startswith('#'),
                              [n.strip() for n in f.readlines()])
                )
    tc.testslist = tclist
    print tc.testslist

    #get build data from file
    if options.build_data:
        with open(options.build_data, "r") as f:
            loaded = json.load(f)
    else:
        loaded = {
              "d": {"DEPLOY_DIR": "./deploy",
                    "TUNE_PKGARCH": "i586"},
              "pkgmanifest": [],
              "filesdir": "oeqa/runtime/files",
              "imagefeatures": []
        }

    #inject build datastore
    d = MyDataDict()
    for key in loaded["d"].keys():
        d[key] = loaded["d"][key]

    if options.log_dir:
        d["TEST_LOG_DIR"] = os.path.abspath(options.log_dir)
    else:
        d["TEST_LOG_DIR"] = os.path.abspath(os.path.dirname(__file__))
    if options.deploy_dir:
        d["DEPLOY_DIR"] = os.path.abspath(options.deploy_dir)
    else:
        if not os.path.isdir(d["DEPLOY_DIR"]):
            raise Exception("The path to DEPLOY_DIR does not exists: %s" % d["DEPLOY_DIR"])
    if options.pkgarch:
        d["TUNE_PKGARCH"] = options.pkgarch
    navarch = os.popen("uname -m").read().strip()
    d["TUNE_NATIVE_ARCH"] = "x86_64" if not navarch else navarch
    if options.nativearch:
        d["TUNE_NATIVE_ARCH"] = options.nativearch
    setattr(tc, "d", d)

    #inject build package manifest
    pkgs = [pname.strip() for pname in loaded["pkgmanifest"]]
    setattr(tc, "pkgmanifest", " ".join(pkgs))

    #inject target information
    target = FakeTarget(d)
    target.ip = options.ip if options.ip else "192.168.7.2"
    target.server_ip = options.server_ip if options.server_ip else "192.168.7.1"
    setattr(tc, "target", target)

    #inject others
    for key in loaded.keys():
        if key not in ["testslist", "d", "target", "pkgmanifest"]:
            setattr(tc, key, loaded[key])

    target.exportStart()
    if options.tag:
        taglist = options.tag.split(',')
        runTests_tag(tc, taglist)
    else:
        runTests(tc)

    return 0

if __name__ == "__main__":
    try:
        ret = main()
    except Exception:
        ret = 1
        import traceback
        traceback.print_exc(5)
    sys.exit(ret)
