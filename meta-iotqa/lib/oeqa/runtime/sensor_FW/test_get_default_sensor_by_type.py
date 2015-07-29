'''Verify to get default sensor with specific type trhough api sf_get_default_sensor()'''
import os
from oeqa.utils.helper import get_files_dir
from oeqa.oetest import oeRuntimeTest
import readConfigFile

class TestGetDefaultSensorByType(oeRuntimeTest):
    '''Verify default sensor returned from sf_get_default_sensor()'''
    def testGetDefaultSensorByType(self):
        '''push binary to target and run with argument'''
        mkdir_path = "mkdir -p /opt/sensor-test/apps"
        (status, output) = self.target.run(mkdir_path)
        copy_to_path = os.path.join(get_files_dir(), 'test_get_default_sensor_by_type')
        (status, output) = self.target.copy_to(copy_to_path, \
"/opt/sensor-test/apps/")
        #run test get expected sensor and show it's information
        client_cmd = "/opt/sensor-test/apps/test_get_default_sensor_by_type "\
                     + readConfigFile.ReadConfFile.getSectionValue( 'sensors','sensor-type-id')
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 1, msg="Error messages: %s" % output)
