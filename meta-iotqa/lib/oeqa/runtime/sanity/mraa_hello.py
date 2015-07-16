import os
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import get_files_dir

class Mraa_hello(oeRuntimeTest):
    '''Say hello to mraa library and get platform name through it'''
    def test_mraa_hello(self):
        '''Prepare test binaries to image'''
        (status, output) = self.target.run('mkdir -p /opt/mraa-test/apps/')
        (status, output) = self.target.run('ls /opt/mraa-test/apps/hello_mraa')
        (status,output) = self.target.copy_to(os.path.join(get_files_dir(),
                          'hello_mraa'), "/opt/mraa-test/apps/")
        '''run test mraa app to get the platform information'''
        client_cmd = "/opt/mraa-test/apps/hello_mraa"
        (status, output) = self.target.run(client_cmd)
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

