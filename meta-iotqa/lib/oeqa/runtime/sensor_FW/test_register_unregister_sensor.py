'''Verify register and unregister related scenarios'''
import os
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import get_files_dir

class TestRegisterUnregisterSensor(oeRuntimeTest):
    '''Verify register and unregister related scenarios'''
    def testSensorRegisterDuplicated(self):
        '''Verify can register duplicated sensor in system'''
        mkdir_path = "mkdir -p /opt/sensor-test/apps/"
        (status, output) = self.target.run(mkdir_path)
        copy_to_path = os.path.join(get_files_dir(), 'test_sensor_register_duplicated')
        (status, output) = self.target.copy_to(copy_to_path, "/opt/sensor-test/apps/")
        client_cmd = "/opt/sensor-test/apps/test_sensor_register_duplicated"
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 1, msg="Error messages: %s" % output)

    def testSensorRegisterUnregisterMisc(self):
        '''Verify misc sensor can be registered in system'''
        mkdir_path = "mkdir -p /opt/sensor-test/apps"
        (status, output) = self.target.run(mkdir_path)
        copy_to_path = os.path.join(get_files_dir(), 'test_sensor_register_unregister_misc')
        (status, output) = self.target.copy_to(copy_to_path, \
"/opt/sensor-test/apps/")
        #run command on target device and check the result
        client_cmd = "/opt/sensor-test/apps/test_sensor_register_unregister_misc"
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 1, msg="Error messages: %s" % output)

    def testUnregisterUnregisteredSensor(self):
        '''Verify sensor can't be unregistered if it's not registered'''
        mkdir_path = "mkdir -p /opt/sensor-test/apps/"
        (status, output) = self.target.run(mkdir_path)
        copy_to_path = os.path.join(get_files_dir(), 'test_unregister_unregistered_sensor')
        (status, output) = self.target.copy_to(copy_to_path, "/opt/sensor-test/apps/")
        client_cmd = "/opt/sensor-test/apps/test_unregister_unregistered_sensor"
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 1, msg="Error messages: %s" % output)
