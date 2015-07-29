'''Verify get sensor raw data'''
import os
from oeqa.utils.helper import get_files_dir
import readConfigFile
from oeqa.oetest import oeRuntimeTest

class TestGetSensorRawDataByID(oeRuntimeTest):
    '''Verify raw sensor data can be returned by sensor id'''
    def testGetSensorRawDataByID(self):
        '''push binary to target and run it with argument'''
        #Prepare test binaries to image        
        mkdir_path = "mkdir -p /opt/sensor-test/apps/"
        (status, output) = self.target.run(mkdir_path)
        copy_path = os.path.join(get_files_dir(), 'test_get_sensor_raw_data_by_id')
        (status, output) = self.target.copy_to(copy_path, \
"/opt/sensor-test/apps/")
        #run test get sensor raw data by id and show it's information
        client_cmd = "/opt/sensor-test/apps/test_get_sensor_raw_data_by_id " \
                     + readConfigFile.ReadConfFile.getSectionValue( 'sensors','valid-id')
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 1, msg="Error messages: %s" % output)
