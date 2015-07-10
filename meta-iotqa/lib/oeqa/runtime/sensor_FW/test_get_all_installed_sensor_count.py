'''Verify to get total count of all installed sensors in system'''
import os
from oeqa.oetest import oeRuntimeTest

class TestGetAllInstalledSensorCount(oeRuntimeTest):
    '''Verify total number of sensors installed in system'''
    def test(self):
        '''push binary to target and run with argument'''
        mkdir_path = "mkdir -p /opt/sensor-test/apps"
        (status, output) = self.target.run(mkdir_path)
        copy_to_path = os.path.join(get_files_dir(), 'test_get_all_installed_sensor_count')
        (status, output) = self.target.copy_to(copy_to_path, \
"/opt/sensor-test/apps/")
        #run test get all installed sensor count and show it's information
        client_cmd = "/opt/sensor-test/apps/test_get_all_installed_sensor_count "
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 1, msg="Error messages: %s" % output)
