'''Verify sensor count returned from sf_get_sensor_count'''
import os
from oeqa.utils.helper import get_files_dir
from oeqa.oetest import oeRuntimeTest
import readConfigFile

class TestGetSensorCountByType(oeRuntimeTest):
    '''Verify sensor count of input type returned from sf_get_sensor_count'''
    def testGetSensorCountByType(self):
        '''Verify sensor count of input type returned from sf_get_sensor_count'''
        mkdir_path = "mkdir -p /opt/sensor-test/apps"
        (status, output) = self.target.run(mkdir_path)
        copy_to_path = os.path.join(get_files_dir(), 'test_get_sensor_count_by_type')
        (status, output) = self.target.copy_to(copy_to_path, \
"/opt/sensor-test/apps/")
        #run test get sensor count by valid type id and show it's information
        client_cmd = "/opt/sensor-test/apps/test_get_sensor_count_by_type "\
                     + readConfigFile.ReadConfFile.getSectionValue( 'sensors','sensor-type-id')
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 1, msg="Error messages: %s" % output)
