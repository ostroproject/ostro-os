'''Verify can't disconnect a sensow which haven't been connected'''
import os
from oeqa.utils.helper import get_files_dir
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.ddt import ddt, file_data
@ddt
class TestDisconnectUnconnectedSensor(oeRuntimeTest):
    '''Verify fail to disconnect a sensor not connected'''
    @file_data('sensor_id.json')
    def testDisconnectUnconnectedSensor(self, value):
        '''Verify fail to disconnect a sensor not connected'''
        mkdir_path = "mkdir -p /opt/sensor-test/apps"
        (status, output) = self.target.run(mkdir_path)
        copy_to_path = os.path.join(get_files_dir(), 'test_disconnect_unconnected_sensor')
        (status, output) = self.target.copy_to(copy_to_path, \
"/opt/sensor-test/apps/")
        cmd = "/opt/sensor-test/apps/test_disconnect_unconnected_sensor"
        client_cmd = "%s %s"%(cmd, str(value))
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 1, msg="Error messages: %s" % output)
