'''Verify api sf_get_sensor_type_by_id'''
import os
from oeqa.utils.helper import get_files_dir
from oeqa.oetest import oeRuntimeTest
from ddt import ddt, file_data
@ddt
class TestGetSensorType(oeRuntimeTest):
    '''Verify sensor type can be returned based on sensor id'''
    @file_data('sensor_id.json')
    def testGetSensorTypeById(self, value):
        '''Verify sensor type can be returned based on sensor id'''
        mkdir_path = "mkdir -p /opt/sensor-test/apps"
        (status, output) = self.target.run(mkdir_path)
        copy_to_path = os.path.join(get_files_dir(), 'test_get_sensor_type_by_id')
        (status, output) = self.target.copy_to(copy_to_path, \
"/opt/sensor-test/apps/")
        #run test get sensor type by id and show it's information
        cmd = "/opt/sensor-test/apps/test_get_sensor_type_by_id"
        client_cmd = "%s %s"%(cmd, str(value))
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 1, msg="Error messages: %s" % output)

    @file_data('invalid_sensor_id.json')
    def testGetSensorTypeByInvalidId(self, value):
        '''Verify eorror returned based on invalid sensor id'''
        mkdir_path = "mkdir -p /opt/sensor-test/apps"
        (status, output) = self.target.run(mkdir_path)
        copy_to_path = os.path.join(get_files_dir(), 'test_get_sensor_type_by_id')
        (status, output) = self.target.copy_to(copy_to_path, \
"/opt/sensor-test/apps/")
        #run test get sensor type by id and show it's information
        cmd = "/opt/sensor-test/apps/test_get_sensor_type_by_id"
        client_cmd = "%s %s"%(cmd, str(value))
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

