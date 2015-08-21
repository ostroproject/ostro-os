'''negatively verify api sf_get_sensor_name'''
import os
from oeqa.utils.helper import get_files_dir
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.ddt import ddt, file_data
@ddt
class TestGetSensorNameByInvalidId(oeRuntimeTest):
    '''Verify sensor name won't be returned if sensor id is invalid'''
    @file_data('invalid_sensor_id.json')
    def testGetSensorNameByInvalidId(self, value):
        '''Verify sensor name won't be returned if sensor id is invalid'''
        mkdir_path = "mkdir -p /opt/sensor-test/apps/"
        (status, output) = self.target.run(mkdir_path)
        copy_to_path = os.path.join(get_files_dir(), 'test_get_sensor_name_by_id')
        (status, output) = self.target.copy_to(copy_to_path, "/opt/sensor-test/apps/")
        #run test get sensor name by invalid id and show it's information
        client_cmd = "/opt/sensor-test/apps/test_get_sensor_name_by_id " \
                     + str(value)
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
