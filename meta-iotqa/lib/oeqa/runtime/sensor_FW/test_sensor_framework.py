'''Verify sensor framework is working'''
import os
import json
from oeqa.utils.helper import get_files_dir
from oeqa.oetest import oeRuntimeTest

class TestSensorFramework(oeRuntimeTest):
    '''Verify sensor framework works in target platform'''
    def testSensorFrameworkReady(self):
        '''Verify sensor framework works in target platform'''
        mkdir_path = "mkdir -p /opt/sensor-test/apps"
        (status, output) = self.target.run(mkdir_path)
        copy_to_path = os.path.join(get_files_dir(), 'test_sensor_framework_ready')
        (status, output) = self.target.copy_to(copy_to_path, \
"/opt/sensor-test/apps/")
        #run test sensor framework ready and show it's information
        client_cmd = "/opt/sensor-test/apps/test_sensor_framework_ready "
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 1, msg="Error messages: %s" % output)
    def testSensorFrameworkRestart(self):
        '''Verify sensor framework works fine after restart'''
        mkdir_path = "mkdir -p /opt/sensor-test/apps"
        (status, output) = self.target.run(mkdir_path)
        copy_to_path = os.path.join(get_files_dir(), 'test_get_sensor_data_by_id')
        (status, output) = self.target.copy_to(copy_to_path, \
"/opt/sensor-test/apps/")
        fp = os.path.join(os.path.dirname(__file__), "sensor_id.json")
        jsf = json.load(file(fp))
        #run test sensor framework ready and show it's information
        cmd = "/opt/sensor-test/apps/test_get_sensor_data_by_id "
        client_cmd = "%s %s"%(cmd, jsf[0])
        (status, output) = self.target.run(client_cmd)
        #test can get sensor data when sensord is started
        self.assertEqual(status, 1, msg="Error messages: %s" % output)
        #restart sensord
        restart_cmd = "systemctl restart sensord"
        (status, output) = self.target.run(restart_cmd)
        print "\n"
        print output
        print restart_cmd, status
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
        #test can get sensor data after sensord is restarted
        (status, output) = self.target.run(client_cmd)
        print "\n"
        print client_cmd
        print output
        self.assertEqual(status, 1, msg="Error messages: %s" % output)

