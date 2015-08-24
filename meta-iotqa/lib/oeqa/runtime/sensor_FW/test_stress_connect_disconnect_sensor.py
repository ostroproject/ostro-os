'''stress testing for connect and disconnect sensor'''
import os
from oeqa.utils.helper import get_files_dir
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.ddt import ddt, file_data
@ddt
class TestStressConnectDisconnectSensor(oeRuntimeTest):
    '''Verify sensor can connected and disconencted 100 times'''
    @file_data('sensor_id.json')
    def testStressConnectDisconnectSensor(self, value):
        '''Verify sensor can connected and disconencted 100 times'''
        mkdir_path = "mkdir -p /opt/sensor-test/apps"
        (status, output) = self.target.run(mkdir_path)
        copy_to_path = os.path.join(get_files_dir(), 'test_stress_connect_disconnect_sensor')
        (status, output) = self.target.copy_to(copy_to_path, \
"/opt/sensor-test/apps/")
        #run test stress connect disconnect sensor and show it's information
        cmd = "/opt/sensor-test/apps/test_stress_connect_disconnect_sensor"
        client_cmd = "%s %s"%(cmd, str(value))
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 1, msg="Error messages: %s" % output)
