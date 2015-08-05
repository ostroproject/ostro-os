'''Verify can't connect to sensor with invalid id'''
import os
from oeqa.utils.helper import get_files_dir
from oeqa.oetest import oeRuntimeTest
import readConfigFile

class TestConnectSensorInvalidId(oeRuntimeTest):
    '''Verify fail to connect sensor with invalid id'''
    def testConnectSensorInvalidId(self):
        '''Verify fail to connect sensor with invalid id'''
        mkdir_path = "mkdir -p /opt/sensor-test/apps"
        (status, output) = self.target.run(mkdir_path)
        copy_to_path = os.path.join(get_files_dir(), 'test_get_sensor_status_by_id')
        (status, output) = self.target.copy_to(copy_to_path, \
"/opt/sensor-test/apps/")
        #run test and verify connection failure if sensor id is invalid
        client_cmd = "/opt/sensor-test/apps/test_get_sensor_status_by_id " \
                     + readConfigFile.ReadConfFile.getSectionValue( 'sensors','invalid-id')
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 2, msg="Error messages: %s" % output)
