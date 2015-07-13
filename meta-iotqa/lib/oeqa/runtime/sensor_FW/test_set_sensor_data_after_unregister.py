'''Verify fail to set sensor data if sensor is unregistered'''
import os
from oeqa.oetest import oeRuntimeTest

class TestSetSensorDataAfterUnregister(oeRuntimeTest):
    '''Verify can't set data to sensor after it's unregistered'''
    def test(self):
        '''push binary to target and run with argument'''
        mkdir_path = "mkdir -p /opt/sensor-test/apps"
        (status, output) = self.target.run(mkdir_path)
        copy_to_path = os.path.join(get_files_dir(), 'test_set_sensor_data_after_unregister')
        (status, output) = self.target.copy_to(copy_to_path, \
"/opt/sensor-test/apps/")
        client_cmd = "/opt/sensor-test/apps/test_set_sensor_data_after_unregister"
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
