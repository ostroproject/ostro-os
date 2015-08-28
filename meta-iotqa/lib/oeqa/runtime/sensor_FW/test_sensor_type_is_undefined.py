'''negatively verify sf_sensor_type_is_supported'''
import os
from oeqa.utils.helper import get_files_dir
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.ddt import ddt, file_data
@ddt
class TestSensorTypeIsUndefined(oeRuntimeTest):
    '''Verify sensor type is unsupported in sensor framework of Ostro OS'''
    @file_data('invalid_sensor_type.json')
    def testSensorTypeIsUndefined(self, value):
        '''Verify sensor type is unsupported in sensor framework of Ostro OS'''
        mkdir_path = "mkdir -p /opt/sensor-test/apps/"
        (status, output) = self.target.run(mkdir_path)
        copy_to_path = os.path.join(get_files_dir(), 'test_sensor_type_is_supported')
        (status, output) = self.target.copy_to(copy_to_path,\
"/opt/sensor-test/apps/")
        #run test sensor type is supported by providing sensor type id
        cmd = "/opt/sensor-test/apps/test_sensor_type_is_supported"
        client_cmd = "%s %s"%(cmd, str(value))
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
