import unittest
import os
import re
from oeqa.oetest import oeRuntimeTest



class SanityTestPython(oeRuntimeTest):
    
    apprt_test_python_helloworld = 'apprt_test_python_helloworld.py'
    apprt_test_python_file = 'apprt_test_python_file.py'
    apprt_test_python_stdout = 'apprt_test_python_stdout.py'
    
    apprt_test_python_helloworld_target = '/tmp/%s' % apprt_test_python_helloworld
    apprt_test_python_file_target = '/tmp/%s' % apprt_test_python_file
    apprt_test_python_stdout_target =  '/tmp/%s' % apprt_test_python_stdout
    apprt_apprt_test_python_file_gen = '/tmp/apprt_test_python_file.python'
    
    def setUp(self):
        self.target.copy_to(os.path.join(os.path.dirname(__file__), 'files', SanityTestPython.apprt_test_python_helloworld), 
        												SanityTestPython.apprt_test_python_helloworld_target
        												)
        self.target.copy_to(os.path.join(os.path.dirname(__file__), 'files', SanityTestPython.apprt_test_python_file), 
        												SanityTestPython.apprt_test_python_file_target
        												)
        self.target.copy_to(os.path.join(os.path.dirname(__file__), 'files', SanityTestPython.apprt_test_python_stdout), 
        												SanityTestPython.apprt_test_python_stdout_target
        												)


    def test_python_exists(self):
        (status, output) = self.target.run('which python')
        self.assertEqual(status, 0, msg = 'python binary not in PATH or on target.')


    def test_python_version(self):
        (status, output) = self.target.run('python -V')
        self.assertEqual(status, 0, msg = 'V option for python command is invalid or python binary does not work.')
        (py, ver) = re.split('\s+', output.strip())
        (major, minor, micro) = re.split('\.', ver.strip())
        self.assertTrue((major > 2) or (major == 2 and minor >= 7), msg = 'Python version is lower than 2.7!') 


    def test_python_file(self):
        (status, output) = self.target.run('python %s' % SanityTestPython.apprt_test_python_file_target)
        self.assertEqual(status, 0, msg = 'Python test file generate failed.')
        self.assertEqual(output, SanityTestPython.apprt_apprt_test_python_file_gen, msg = '/tmp/apprt_test_python_file.python generate failed!')


    def test_python_stdout(self):
        (status, output) = self.target.run('python %s' % SanityTestPython.apprt_test_python_stdout_target)
        self.assertEqual(status, 0, msg = 'Exit status was not 0. Output: %s' % output)
        self.assertEqual(output, 'the value of a is 0.01', msg = 'Incorrect output: %s' % output)

        
    def test_python_helloworld(self):
        (status, output) = self.target.run('python %s' % SanityTestPython.apprt_test_python_helloworld_target)
        self.assertEqual(status, 0, msg = 'Exit status was not 0. Output: %s' % output)
        self.assertEqual(output, 'Hello World!', msg = 'Incorrect output: %s' % output)
        

    def tearDown(self):
        self.target.run('rm -f %s %s %s %s' % (SanityTestPython.apprt_test_python_helloworld_target, 
        																		SanityTestPython.apprt_test_python_file_target, 
        																		SanityTestPython.apprt_test_python_stdout_target,
        																		SanityTestPython.apprt_apprt_test_python_file_gen))


