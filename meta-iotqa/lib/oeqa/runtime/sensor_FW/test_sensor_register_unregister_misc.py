'''Verify can register a misc sensor in system  successfully'''
import os
from oeqa.utils.helper import get_files_dir
from oeqa.oetest import oeRuntimeTest

class TestSensorRegisterUnregisterMisc(oeRuntimeTest):
    '''Verify misc sensor can be registered in system'''
    def testSensorRegisterUnregisterMisc(self):
        '''Verify misc sensor can be registered in system'''
        mkdir_path = "mkdir -p /opt/sensor-test/apps"
        (status, output) = self.target.run(mkdir_path)
        copy_to_path = os.path.join(get_files_dir(), 'test_sensor_register_unregister_misc')
        (status, output) = self.target.copy_to(copy_to_path, \
"/opt/sensor-test/apps/")
        #run command on target device and check the result
        client_cmd = "/opt/sensor-test/apps/test_sensor_register_unregister_misc"
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 1, msg="Error messages: %s" % output)
