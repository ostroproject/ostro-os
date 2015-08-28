'''Verify to get sensors with specific type trhough api sf_get_sensor_list()'''
import os
from oeqa.utils.helper import get_files_dir
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.ddt import ddt, file_data
@ddt
class TestGetSensorListByType(oeRuntimeTest):
    '''Verify sensors with specific type can be returned'''
    @file_data('sensor_type.json')
    def testGetSensorListByType(self, value):
        '''Verify sensors with specific type can be returned'''
        mkdir_path = "mkdir -p /opt/sensor-test/apps"
        (status, output) = self.target.run(mkdir_path)
        copy_to_path = os.path.join(get_files_dir(), 'test_get_sensor_list_by_type')
        (status, output) = self.target.copy_to(copy_to_path, \
"/opt/sensor-test/apps/")
        #run test get expected sensor list and show it's information
        cmd = "/opt/sensor-test/apps/test_get_sensor_list_by_type"
        client_cmd = "%s %s"%(cmd, str(value))
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 1, msg="Error messages: %s" % output)
