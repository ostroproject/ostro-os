'''Verify sensor framework is working'''
import os
from oeqa.utils.helper import get_files_dir
from oeqa.oetest import oeRuntimeTest

class TestSensorFrameworkReady(oeRuntimeTest):
    '''Verify sensor framework works in target platform'''
    def testSensorFrameworkReady(self):
        '''Verify sensor framework works in target platform'''
        mkdir_path = "mkdir -p /opt/sensor-test/apps"
        (status, output) = self.target.run(mkdir_path)
        copy_to_path = os.path.join(get_files_dir(), 'test_sensor_framework_ready')
        (status, output) = self.target.copy_to(copy_to_path, \
"/opt/sensor-test/apps/")
        #run test sensor framework ready and show it's information
        client_cmd = "/opt/sensor-test/apps/test_sensor_framework_ready "
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 1, msg="Error messages: %s" % output)
