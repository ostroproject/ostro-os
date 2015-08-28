'''Verify error happens if try to disconnect non-exist sensor'''
import os
from oeqa.utils.helper import get_files_dir
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.ddt import ddt, file_data
@ddt
class TestDisconnectSensorInvalidId(oeRuntimeTest):
    '''Verify fail to disconnect non exist sensor'''
    @file_data('invalid_sensor_id.json')
    def testDisconnectSensorInvalidId(self, value):
        '''Verify fail to disconnect non exist sensor'''
        mkdir_path = "mkdir -p /opt/sensor-test/apps"
        (status, output) = self.target.run(mkdir_path)
        copy_to_path = os.path.join(get_files_dir(), 'test_disconnect_sensor_invalid_id')
        (status, output) = self.target.copy_to(copy_to_path, \
"/opt/sensor-test/apps/")
        cmd = "/opt/sensor-test/apps/test_disconnect_sensor_invalid_id"
        client_cmd = "%s %s"%(cmd, str(value))
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
