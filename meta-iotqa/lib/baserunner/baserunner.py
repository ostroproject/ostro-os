#!/usr/bin/env python
# Copyright (C) 2013 Intel Corporation
#
# Released under the MIT license (see COPYING.MIT)

# Base unittest module used by testrunner
# This provides the common test runner functionalities including manifest input,
# xunit output, timeout, tag filtering.

"""Base testrunner"""

import os
import sys
import time
import unittest
import shutil
from optparse import OptionParser, make_option
from util.log import LogHandler
from util.tag import filter_tagexp
from util.timeout import set_timeout

class TestContext(object):
    '''test context which inject into testcase'''
    def __init__(self):
        self.target = None
        self.def_timeout = None

class TestRunnerBase(object):
    '''test runner base '''
    def __init__(self, context=None):
        self.tclist = []
        self.runner = None
        self.context = context if context else TestContext()
        self.test_options = None
        self.log_handler = None
        self.test_result = None
        self.run_time = None
        self.option_list = [
            make_option("-f", "--manifest", dest="manifest",
                        help="The test list file"),
            make_option("-x", "--xunit", dest="xunit",
                        help="Output result path of in xUnit XML format"),
            make_option("-l", "--log-dir", dest="logdir",
                        help="Set log dir."),
            make_option("-a", "--tag-expression", dest="tag",
                        help="Set tag expression to filter test cases."),
            make_option("-T", "--timeout", dest="timeout", default=60,
                        help="Set timeout for each test case."),
            make_option("-e", "--tests", dest="tests", action="append",
                        help="Run tests by dot separated module path")
        ]

    def __del__(self):
        """
        Because unittest.TestCase is a class object, it will exist as long as the python virtual machine process.
        So tc can't be released if we don't release them explicitly.
        """
        if hasattr(unittest.TestCase, "tc"):
            delattr(unittest.TestCase, "tc")

    @staticmethod
    def __get_tc_from_manifest(fname):
        '''get tc list from manifest format '''
        with open(fname, "r") as f:
            tclist = [n.strip() for n in f.readlines() \
                                if n.strip() and not n.strip().startswith('#')]
        return tclist

    @staticmethod
    def _get_log_dir(logdir):
        '''get the log directory'''
        if os.path.exists(logdir):
            shutil.rmtree(logdir)
        os.makedirs(logdir)
        return logdir

    def get_options(self, default=False):
        '''handle testrunner options'''
        parser = OptionParser(option_list=self.option_list, \
                                usage="usage: %prog [options]")
        if default:
            return parser.parse_args(args=[])[0]
        return parser.parse_args()[0]

    def configure(self, options):
        '''configure before testing'''
        self.test_options = options
        if options.xunit:
            try:
                from xmlrunner import XMLTestRunner
            except ImportError:
                raise Exception("unittest-xml-reporting not installed")
            self.runner = XMLTestRunner(stream=sys.stderr, \
                                        verbosity=2, output=options.xunit)
        else:
            self.runner = unittest.TextTestRunner(stream=sys.stderr, \
                                                  verbosity=2)

        if options.manifest:
            fbname, fext = os.path.splitext(os.path.basename(options.manifest))
            assert fbname == "manifest" or fext == ".manifest", \
                  "Please specify file name like xxx.manifest or manifest.xxx"
            self.tclist = self.__get_tc_from_manifest(options.manifest)

        if options.tests:
            tcs = [t[0:-3] if t.endswith(".py") else t[0:-1] \
                               if t.endswith("/") else t for t in options.tests]
            self.tclist.extend([tc.replace("/", ".") for tc in tcs])

        if options.logdir:
            logdir = self._get_log_dir(options.logdir)
            self.log_handler = LogHandler(logdir)

        try:
            self.context.def_timeout = int(options.timeout)
        except ValueError:
            print "timeout need an integer value"
            raise

    def result(self):
        '''output test result '''
        print "output test result..."

    def loadtest(self, names=None):
        '''load test suite'''
        if not names:
            names = self.tclist
        print "tclist: %s" % names
        testloader = unittest.TestLoader()
        tclist = []
        for name in names:
            tset = testloader.loadTestsFromName(name)
            if tset.countTestCases() > 0:
                tclist.append(tset)
            elif tset._tests == []:
                tclist.append(testloader.discover(name, "[!_]*.py", os.path.curdir))
        return testloader.suiteClass(tclist)

    def filtertest(self, testsuite):
        '''filter test set'''
        if self.test_options.tag:
            return filter_tagexp(testsuite, self.test_options.tag)
        return testsuite

    def runtest(self, testsuite):
        '''run test suite'''
        starttime = time.time()
        self.test_result = self.runner.run(testsuite)
        self.run_time = time.time() - starttime

    def start(self, testsuite):
        '''start testing'''
        if self.log_handler:
            self.log_handler.start()
        set_timeout(testsuite, self.context.def_timeout)
        setattr(unittest.TestCase, "tc", self.context)
        self.runtest(testsuite)
        self.result()
        if self.log_handler:
            self.log_handler.end()

if __name__ == "__main__":
    runner = TestRunnerBase()
    opts = runner.get_options()
    runner.configure(opts)
    suite = runner.filtertest(runner.loadtest())
    print "Found %s tests" % suite.countTestCases()
    runner.start(suite)
