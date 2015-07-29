'''Test case to verify get default sensor by type and manipulate it'''
import os
from oeqa.utils.helper import get_files_dir
from oeqa.oetest import oeRuntimeTest
import readConfigFile

class TestGetDefaultSensorAndManipulation(oeRuntimeTest):
    '''Verify user can manipulate default sensor of a specific type'''
    def testGetDefaultSensorAndManipulation(self):
        '''push binary file to target and run with argument'''
        #Prepare test binaries to image
        mkdir_path = 'mkdir -p /opt/sensor-test/apps/'
        (status, output) = self.target.run(mkdir_path)
        copy_path = os.path.join(get_files_dir(), 'test_get_default_sensor_and_manipulation')
        (status, output) = self.target.copy_to(copy_path,\
"/opt/sensor-test/apps/")
        #run test and show related information
        client_cmd = \
"/opt/sensor-test/apps/test_get_default_sensor_and_manipulation "\
                     + readConfigFile.ReadConfFile.getSectionValue( 'sensors','sensor-type-id')
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 1, msg="Error messages: %s" % output)
