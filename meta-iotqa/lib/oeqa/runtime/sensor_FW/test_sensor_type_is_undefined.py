'''negatively verify sf_sensor_type_is_supported'''
import os
from oeqa.oetest import oeRuntimeTest
import readConfigFile

class TestSensorIsUndefined(oeRuntimeTest):
    '''Verify sensor type is unsupported in sensor framework of Ostro OS'''
    def test(self):
        '''push binary to target and run with argument'''
        mkdir_path = "mkdir -p /opt/sensor-test/apps/"
        (status, output) = self.target.run(mkdir_path)
        copy_to_path = os.path.join(get_files_dir(), 'test_sensor_type_is_supported')
        (status, output) = self.target.copy_to(copy_to_path,\
"/opt/sensor-test/apps/")
        #run test sensor type is supported by providing sensor type id
        client_cmd = "/opt/sensor-test/apps/test_sensor_type_is_supported "\
                     + readConfigFile.ReadConfFile.getSectionValue( 'sensors','invalid-id')
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
