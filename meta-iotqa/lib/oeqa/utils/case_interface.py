"""
This module provide some API for help run some not py-unit based testcases.
"""
import sys
import unittest
from oeqa.oetest import oeRuntimeTest

class FakeResult(object):
    "It's a fake result object, used in TestCaseInterface to hiden called test method"
    def __getattr__(self, name):
        return self
    def __call__(self, *args, **kwargs):
        return self

class ErrorException(Exception):
    pass

def genTestObj(classname, testname, func=lambda self:None):
    cls = type(classname, (oeRuntimeTest,), {testname: func})
    return cls(testname)

class TestCaseInterface(oeRuntimeTest):
    """
    usage:
    for example:
    class MyUpstreamTestCase(TestCaseInterface):
        # this case(testUpstream) wasn't showed in result
        def testUpstream(self):
            #run and parse some cases
            #use self.addSuccess to add success case
            #...
    """
    def run(self, result, *args, **kwargs):
        self.result = result
        ori = unittest.TestCase.run
        ori(self, FakeResult(), *args, **kwargs)

    def addSuccess(self, casename, classname=None, stdout="", stderr=""):
        classname = classname if classname else casename
        def testFake(self):
            sys.stdout.write(stdout)
            sys.stderr.write(stderr)
        obj = genTestObj(classname, casename, testFake)
        obj.run(self.result)

    def addError(self, casename, classname=None, stdout="", stderr=""):
        classname = classname if classname else casename
        def testFake(self):
            sys.stdout.write(stdout)
            sys.stderr.write(stderr)
            raise ErrorException()
        obj = genTestObj(classname, casename, testFake)
        obj.run(self.result)

    def addFailure(self, casename, classname=None, stdout="", stderr=""):
        classname = classname if classname else casename
        def testFake(self):
            sys.stdout.write(stdout)
            sys.stderr.write(stderr)
            assert False
        obj = genTestObj(classname, casename, testFake)
        obj.run(self.result)

    def addSkip(self, casename, classname=None, stdout="", stderr=""):
        classname = classname if classname else casename
        def testFake(self):
            sys.stdout.write(stdout)
            sys.stderr.write(stderr)
            self.skipTest("")
        obj = genTestObj(classname, casename, testFake)
        obj.run(self.result)

#     def testInterface(self):
#         self.addSuccess("testxx","TestXX", "testxx", "")
#         self.addError("testyy", "TestYY", "", "testyy")
#         self.addFailure("testzz", "TestZZ", "", "")
#         self.addSkip("testskip")

