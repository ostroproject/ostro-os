import os
from oeqa.oetest import oeRuntimeTest

class Mraa_hello(oeRuntimeTest):
    '''Say hello to mraa library and get platform name through it'''
    def test_mraa_hello(self):
        '''Prepare test binaries to image'''
        (status, output) = self.target.run('mkdir -p /opt/mraa-test/apps/')
        (status, output) = self.target.run('ls /opt/mraa-test/apps/mraa-test')
        if status != 0:
            (status,output) = self.target.copy_to(os.path.join(oeRuntimeTest.tc.filesdir,
                          'mraa-test'), "/opt/mraa-test/apps/")
        '''run test mraa app to get the platform information'''
        client_cmd = "/opt/mraa-test/apps/mraa-test"
        (status, output) = self.target.run(client_cmd)
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

