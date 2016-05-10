#!/usr/bin/python
'''
Copyright (c) 2016 Intel Corporation

Created on Mar 15, 2016

@author: zjh
'''
import os, sys
import unittest
import shutil
import collections
from optparse import make_option
from baserunner.baserunner import  TestRunnerBase
from oeqa.oetest import oeTest
from baserunner.util.tag import *
from runtest import *
import glob

def filter_test(func, testsuite):
    caselist = []
    for each in testsuite:
        if unittest.suite._isnotsuite(each):
            if func(each):
                caselist.append(each)
        else:
            caselist.append(filter_test(func, each))
    return testsuite.__class__(caselist)

def split(s, sep=","):
    s = s.strip()
    return [x.strip() for x in s.split(sep) if x.strip()]

def testset(testsuite):
    """interate tcs in testsuite"""
    for each in testsuite:
        if unittest.suite._isnotsuite(each):
            yield each
        else:
            for each2 in testset(each):
                yield  each2

class NameMeta(type):
    def __new__(cls, name, parents, attrs):
        if "name" not in attrs:
            attrs["name"] = name
        return super(NameMeta, cls). __new__(cls, name, parents, attrs)

def getComponent(testcase):
    caseid = testcase.id()
    names = caseid.split(".")
    if len(names)>=3:
        return names[2]
    else:
        print "Do you in an iottest suite folder?"
        return names[-3]

class Platform(object):
    name = None
    __metaclass__ = NameMeta

    def filter_test(self, testcase):
        exp = "(not WhiteList or not WhiteList.strip() or '%s' in [x.strip() for x in WhiteList.split(',')]) and\
        (not BlackList or not BlackList.strip() or '%s' not in [x.strip() for x in BlackList.split(',')])"%(self.name, self.name)
        return checktags(testcase, exp)

class GB_BXBT(Platform):
    name = "GB-BXBT"
class Galileo(Platform):
    pass
class Minnow(Platform):
    pass
class Edsion(Platform):
    pass
class ManifestGener(TestRunnerBase):
    def __init__(self, context=None):
        super(ManifestGener, self).__init__(context)
        self.option_list.extend([
            make_option("-o", "--output-dir", dest="output", default = "manifest_output",
                    help="the output folder, default is manifest_output"),
            make_option("-p", "--platform", dest="platforms", default = [], action="append",
                    help="Platform: Galileo, Minnow.."),
            make_option("--list", dest="list", action="store_true",
                    help="list all components"),
            make_option("-s", "--component", dest="components", default = [], action="append",
                    help="Whick components shold be generate.")])

    def init_context(self):
        builddata_files = glob.glob(os.path.join(BASEDIR, "deploy", "files", "*", "builddata.json"))
        if builddata_files:
            with open(builddata_files[0], "r") as f:
                loaded = json.load(f)
        else:
            loaded = {"pkgmanifest":[]}
        #inject build datastore
        d = MyDataDict()
        if loaded.has_key("d"):
            for key in loaded["d"].keys():
                d[key] = loaded["d"][key]
        d["DEPLOY_DIR"], d["MACHINE"] = "" , ""
        tc = TestContext()
        setattr(tc, "d", d)

        pkgs = [pname.strip() for pname in loaded["pkgmanifest"]]
        setattr(tc, "pkgmanifest", "\n".join(pkgs))

        setattr(tc, "targets", [])
        setattr(tc, "target", None)
        setattr(oeRuntimeTest, "targets", [])
    
        #inject others
        for key in loaded.keys():
            if key not in ["testslist", "d", "target", "pkgmanifest"]:
                setattr(tc, key, loaded[key])
        self.context = tc
        oeTest.tc = tc

    def configure(self, options):
        options.tests = ["oeqa.runtime"] if not options.tests else options.tests
        self.init_context()
        super(ManifestGener, self).configure(options)
        self.output = options.output
        self.tagexp = options.tag
        platforms = [cls() for cls in Platform.__subclasses__()]
        options.platforms = list(set([x.strip() for x in options.platforms]))
        if options.platforms:
            self.platforms = []
            for platform in options.platforms:
                for platform_obj in platforms:
                    if platform == platform_obj.name:
                        self.platforms.append(platform_obj)
                        break
                else:
                    print "Warring: Can't find platform: %s"%platform
                    self.platforms.append(type(platform, (Platform,), {})())
        else:
            self.platforms = platforms
        self.components = options.components

    def list_components(self):
        runtime_path = os.path.join(os.path.dirname(__file__), "oeqa", "runtime")
        print "%-20s    %s"%("Compont","description")
        for name in os.listdir(runtime_path):
            p = os.path.join(runtime_path, name)
            if os.path.isdir(p) or (not name.startswith("_") and name.endswith(".py")):
                if os.path.isfile(p):
                    name = name[:-3]
                try:
                    testsuite = self.loadtest(["oeqa.runtime."+name])
                    if testsuite.countTestCases()>0:
                        m = __import__("oeqa.runtime."+name)
                        component = name
                        doc = m.__doc__
                        print "%-20s    %s" % (component, doc.splitlines()[0] if doc else "This is %s component"%component)
                except:
                    pass

    def gen_manifest(self, testsuite):
        if os.path.lexists(self.output):
            shutil.rmtree(self.output)
        os.mkdir(self.output)
        testsuite = self.filter_test_by_components(testsuite)
        testsuite = self.filtertest(testsuite)
        testsuite = self.filter_error(testsuite)
        print "Detect %s test cases." % testsuite.countTestCases()
        print "%-50s %s" % ("Manifest file", "Test cases number")
        for platform in self.platforms:
            platform_suite = filter_test(platform.filter_test, testsuite)
            self.write_to_file(platform.name, platform_suite)

    def sort_by_compont(self, testsuite):
        ret = collections.OrderedDict()
        for case in testset(testsuite):
            key = getComponent(case)
            ret.setdefault(key, []).append(case)
        return ret

    def write_to_file(self, filename, testsuite):
        filename = filename + ".manifest"
        filename = os.path.join(self.output, filename)
        with open(filename, "w") as f:
            f.write("# This manifest file is generated by: %s\n" % " ".join(sys.argv))
            f.write("# All test cases number: %s\n" % testsuite.countTestCases())
            f.write(os.linesep)
            print "%-50s %s"%(filename, testsuite.countTestCases())
            for component, cases in self.sort_by_compont(testsuite).items():
                f.write("## @Component: %s;"%component)
                f.write(os.linesep)
                for case in cases:
                    f.write(case.id())
                    f.write(os.linesep)
                f.write(os.linesep)

    def filter_error(self, testsuite):
        """
        Some cases failed when loaded, but unittest.loadtest had wrap this error
        to a test object. This method will remove them and print these errors.
        """
        def _filter_error(testcase):
            if testcase.__class__.__name__ in ('ModuleImportFailure', 'LoadTestsFailure'):
                try:
                    getattr(testcase, testcase._testMethodName)()
                except BaseException, e:
                    print e
                    return False
            return True
        return filter_test(_filter_error, testsuite)

    def filter_test_by_tag(self, testsuite, tagexp):
        '''filter test set'''
        return filter_tagexp(testsuite, tagexp)

    def filter_test_by_components(self, testsuite, components=None):
        '''filter test set'''
        components = self.components if not components else components
        def _filter_components(testcase):
            return getComponent(testcase) in components
        return filter_test(_filter_components, testsuite)

if __name__ == '__main__':
    gener = ManifestGener()
    opts = gener.get_options()
    gener.configure(opts)
    if opts.list:
        gener.list_components()
    else:
        gener.gen_manifest(gener.loadtest())
