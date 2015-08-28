'''Verify maximum connections to sensor is 64'''
import os
from oeqa.utils.helper import get_files_dir
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.ddt import ddt, file_data
@ddt
class TestConnectSensorMaximumTimes(oeRuntimeTest):
    '''Verify maximum connections allowed to sensor is 64'''
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
