"""
This module provide some API for help run some not py-unit based testcases.
"""
import sys
import unittest
from oeqa.oetest import oeRuntimeTest

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
        _result = unittest.TextTestResult(unittest.runner._WritelnDecorator(sys.stderr), True, 1)
        ori(self, _result, *args, **kwargs)
        _result.stopTestRun()
        _result.printErrors()

    def addCase(self, func, casename, classname=None, stdout="", stderr=""):
        casename = casename.strip()
        classname = classname if classname else casename
        def testFake(self):
            sys.stdout.write(stdout)
            sys.stderr.write(stderr)
            func()
        obj = genTestObj(classname, casename, testFake)
        obj.run(self.result)

    def addSuccess(self, *args, **kwargs):
        def success():
            pass
        return self.addCase(success, *args, **kwargs)

    def addError(self, *args, **kwargs):
        def error():
            raise ErrorException()
        return self.addCase(error, *args, **kwargs)

    def addFailure(self, *args, **kwargs):
        def failure():
            assert False
        return self.addCase(failure, *args, **kwargs)

    def addSkip(self, *args, **kwargs):
        def skip():
            self.skipTest("")
        return self.addCase(skip, *args, **kwargs)

#     def testInterface(self):
#         self.addSuccess("testxx","TestXX", "testxx", "")
#         self.addError("testyy", "TestYY", "", "testyy")
#         self.addFailure("testzz", "TestZZ", "", "")
#         self.addSkip("testskip")

