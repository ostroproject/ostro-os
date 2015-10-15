'''Verify connect sensor under different scenarios'''
import os
import json
from oeqa.utils.helper import get_files_dir
from oeqa.oetest import oeRuntimeTest
from ddt import ddt, file_data
@ddt
class TestConnectSensor(oeRuntimeTest):
    '''Verify connect sensor under different scenarios'''
    @file_data('sensor_id.json')
    def testConnectSensorAlreadyConnected(self, value):
        '''check connect sensor if it's already connected'''
        #Prepare test binaries to image        
        mkdir_path = "mkdir -p /opt/sensor-test/apps/"
        (status, output) = self.target.run(mkdir_path)
        copy_path = os.path.join(get_files_dir(), 'test_connect_sensor_already_connected')
        (status, output) = self.target.copy_to(copy_path, \
"/opt/sensor-test/apps/")
        #run test get sensor by id and show it's information
        cmd = "/opt/sensor-test/apps/test_connect_sensor_already_connected"
        client_cmd = "%s %s"%(cmd, str(value))
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 1, msg="Error messages: %s" % output)    

    @file_data('sensor_id.json')
    def testConnectSensorMaximumTimes(self, value):
        '''Verify maximum connections allowed to sensor is 64'''
        #Prepare test binaries to image        
        mkdir_path = "mkdir -p /opt/sensor-test/apps/"
        (status, output) = self.target.run(mkdir_path)
        copy_path = os.path.join(get_files_dir(), 'test_connect_sensor_maximum_times')
        (status, output) = self.target.copy_to(copy_path, \
"/opt/sensor-test/apps/")
        #run test get sensor by id and show it's information
        cmd = "/opt/sensor-test/apps/test_connect_sensor_maximum_times"
        client_cmd = "%s %s"%(cmd, str(value))
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 1, msg="Error messages: %s" % output)

    @file_data('invalid_sensor_id.json')
    def testConnectSensorInvalidId(self, value):
        '''Verify fail to connect sensor with invalid id'''
        mkdir_path = "mkdir -p /opt/sensor-test/apps"
        (status, output) = self.target.run(mkdir_path)
        copy_to_path = os.path.join(get_files_dir(), 'test_get_sensor_status_by_id')
        (status, output) = self.target.copy_to(copy_to_path, \
"/opt/sensor-test/apps/")
        #run test and verify connection failure if sensor id is invalid
        cmd = "/opt/sensor-test/apps/test_get_sensor_status_by_id"
        client_cmd = "%s %s"%(cmd, str(value))
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 2, msg="Error messages: %s" % output)
