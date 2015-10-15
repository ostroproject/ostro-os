'''Verify default sensor related operations'''
import os
from oeqa.utils.helper import get_files_dir
from oeqa.oetest import oeRuntimeTest
from ddt import ddt, file_data
@ddt
class TestDefaultSensor(oeRuntimeTest):
    '''Verify default sensor related operations'''
    @file_data('sensor_type.json')
    def testGetDefaultSensorByType(self, value):
        '''Verify default sensor returned from sf_get_default_sensor()'''
        mkdir_path = "mkdir -p /opt/sensor-test/apps"
        (status, output) = self.target.run(mkdir_path)
        copy_to_path = os.path.join(get_files_dir(), 'test_get_default_sensor_by_type')
        (status, output) = self.target.copy_to(copy_to_path, \
"/opt/sensor-test/apps/")
        #run test get expected sensor and show it's information
        cmd = "/opt/sensor-test/apps/test_get_default_sensor_by_type"
        client_cmd = "%s %s"%(cmd, str(value))
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 1, msg="Error messages: %s" % output)

    @file_data('invalid_sensor_type.json')
    def testGetDefaultSensorByInvalidType(self, value):
        '''Verify error returns when give invalid type'''
        mkdir_path = "mkdir -p /opt/sensor-test/apps"
        (status, output) = self.target.run(mkdir_path)
        copy_to_path = os.path.join(get_files_dir(), 'test_get_default_sensor_by_type')
        (status, output) = self.target.copy_to(copy_to_path, \
"/opt/sensor-test/apps/")
        #run test get error and show it's information
        cmd = "/opt/sensor-test/apps/test_get_default_sensor_by_type"
        client_cmd = "%s %s"%(cmd, str(value))
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

    @file_data('sensor_type.json')
    def testGetDefaultSensorAndManipulation(self, value):
        '''Verify user can manipulate default sensor of a specific type'''
        #Prepare test binaries to image
        mkdir_path = 'mkdir -p /opt/sensor-test/apps/'
        (status, output) = self.target.run(mkdir_path)
        copy_path = os.path.join(get_files_dir(), 'test_get_default_sensor_and_manipulation')
        (status, output) = self.target.copy_to(copy_path,\
"/opt/sensor-test/apps/")
        #run test and show related information
        cmd = "/opt/sensor-test/apps/test_get_default_sensor_and_manipulation"
        client_cmd = "%s %s"%(cmd, str(value))
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 1, msg="Error messages: %s" % output)
