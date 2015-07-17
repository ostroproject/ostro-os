'''Verify can register sensor with dup name and type'''
import os
from oeqa.utils.helper import get_files_dir
from oeqa.oetest import oeRuntimeTest

class TestSensorRegisterDuplicated(oeRuntimeTest):
    '''Verify can register duplicated sensor in system'''
    def test(self):
        '''push binary to target and run it with argument'''
        #Prepare test binaries to image
        mkdir_path = "mkdir -p /opt/sensor-test/apps/"
        (status, output) = self.target.run(mkdir_path)
        copy_to_path = os.path.join(get_files_dir(), 'test_sensor_register_duplicated')
        (status, output) = self.target.copy_to(copy_to_path, "/opt/sensor-test/apps/")
        client_cmd = "/opt/sensor-test/apps/test_sensor_register_duplicated"
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 1, msg="Error messages: %s" % output)
