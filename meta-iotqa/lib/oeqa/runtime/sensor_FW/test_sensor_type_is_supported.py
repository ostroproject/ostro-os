'''positively verify sf_sensor_type_is_supported'''
import os
from oeqa.utils.helper import get_files_dir
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.ddt import ddt, file_data
@ddt
class TestSensorTypeIsSupported(oeRuntimeTest):
    '''Verify sensor type is supported in sensor framework of Ostro OS'''
    @file_data('sensor_type.json')
    def testSensorTypeIsSupported(self, value):
        '''Verify sensor type is supported in sensor framework of Ostro OS'''
        mkdir_path = "mkdir -p /opt/sensor-test/apps/"
        (status, output) = self.target.run(mkdir_path)
        copy_to_path = os.path.join(get_files_dir(), 'test_sensor_type_is_supported')
        (status, output) = self.target.copy_to(copy_to_path,\
"/opt/sensor-test/apps/")
        #run test sensor type is supported by providing sensor type id
        client_cmd = "/opt/sensor-test/apps/test_sensor_type_is_supported "\
                     + str(value)
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 1, msg="Error messages: %s" % output)
