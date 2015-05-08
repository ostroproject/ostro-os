import unittest
import os
import re
from oeqa.oetest import oeRuntimeTest, skipModule
from oeqa.utils.decorators import *


class PythonHelloWorldTest(oeRuntimeTest):
    
    @classmethod
    def setUpClass(cls):
        oeRuntimeTest.tc.target.copy_to(os.path.join(oeRuntimeTest.tc.filesdir, 'apprt_helloworld.py'), '/tmp/apprt_helloworld.py')
        oeRuntimeTest.tc.target.copy_to(os.path.join(oeRuntimeTest.tc.filesdir, 'apprt_test.py'), '/tmp/apprt_test.py')


    def test_python_exists(self):
        (status, output) = self.target.run('which python')
        self.assertEqual(status, 0, msg = 'python binary not in PATH or on target.')


    def test_python_version(self):
        (status, output) = self.target.run('python -V')
        self.assertEqual(status, 0, msg = 'V option for python command is invalid or python binary does not work.')
        (py, ver) = re.split('\s+', output.strip())
        (major, minor, micro) = re.split('\.', ver.strip())
        self.assertTrue((major > 2) or (major == 2 and minor >= 7), msg = "Python version is lower than 2.7!") 


    def test_python_helloworld(self):
        (status, output) = self.target.run('python /tmp/apprt_helloworld.py')
        self.assertEqual(status, 0, msg = "Exit status was not 0. Output: %s" % output)
        self.assertEqual(output, 'Hello World!', msg = "Incorrect output: %s" % output)


    def test_python_stdout(self):
        (status, output) = self.target.run('python /tmp/apprt_test.py')
        self.assertEqual(status, 0, msg = "Exit status was not 0. Output: %s" % output)
        self.assertEqual(output, 'the value of a is 0.01', msg = "Incorrect output: %s" % output)


    def test_python_testfile(self):
        (status, output) = self.target.run('ls /tmp/testfile.python')
        self.assertEqual(status, 0, msg = "Python test file generate failed.")


    @classmethod
    def tearDownClass(cls):
        oeRuntimeTest.tc.target.run('rm -f /tmp/apprt_helloworld.py /tmp/apprt_test.py /tmp/testfile.python')


