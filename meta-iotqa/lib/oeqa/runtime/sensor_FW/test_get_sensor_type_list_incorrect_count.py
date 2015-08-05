'''Verify error handling when input parameter 'count' is not correct'''
import os
from oeqa.utils.helper import get_files_dir
import readConfigFile
from oeqa.oetest import oeRuntimeTest

class TestGetSensorTypeListIncorrectCount(oeRuntimeTest):
    '''Verify error code return if input paramter 'count' is not correct'''
    def testGetSensorTypeListIncorrectCount(self):
        '''Verify error code return if input paramter 'count' is not correct'''     
        mkdir_path = "mkdir -p /opt/sensor-test/apps/"
        (status, output) = self.target.run(mkdir_path)
        copy_path = os.path.join(get_files_dir(), \
 'test_get_sensor_type_list_incorrect_count')
        (status, output) = self.target.copy_to(copy_path, \
"/opt/sensor-test/apps/")
        client_cmd = "/opt/sensor-test/apps/test_get_sensor_type_list_incorrect_count "
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
