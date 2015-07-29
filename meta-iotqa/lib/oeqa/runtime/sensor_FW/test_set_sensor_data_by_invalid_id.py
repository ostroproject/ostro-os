'''Verify fail to set sensor data if given id is invalid'''
import os
from oeqa.utils.helper import get_files_dir
from oeqa.oetest import oeRuntimeTest
import readConfigFile

class TestSetSensorDataByInvalidId(oeRuntimeTest):
    '''Verify error happens when set data using invalid sensor id'''
    def testSetSensorDataByInvalidId(self):
        '''push binary to target and run it with argument'''
        #Prepare test binaries to image
        mkdir_path = "mkdir -p /opt/sensor-test/apps/"
        (status, output) = self.target.run(mkdir_path)
        copy_to_path = os.path.join(get_files_dir(), 'test_set_sensor_data_by_id')
        (status, output) = self.target.copy_to(copy_to_path, "/opt/sensor-test/apps/")
        #run test set sensor data by invalid id and show it's information
        client_cmd = "/opt/sensor-test/apps/test_set_sensor_data_by_id " \
                     + readConfigFile.ReadConfFile.getSectionValue( 'sensors','invalid-id')
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
