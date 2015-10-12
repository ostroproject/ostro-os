'''Verify switch connecting to different sensors'''
import os
import json
from oeqa.utils.helper import get_files_dir
from oeqa.oetest import oeRuntimeTest

class TestSwitchGetSensorData(oeRuntimeTest):
      '''Verify switch connecting to different sensors'''
      def testSwitchGetSensorData(self):
        '''switch connecting to different sensor without disconnect from first one'''
        #Prepare test binaries to image        
        mkdir_path = "mkdir -p /opt/sensor-test/apps/"
        (status, output) = self.target.run(mkdir_path)
        copy_path = os.path.join(get_files_dir(), 'test_switch_get_sensor_data')
        (status, output) = self.target.copy_to(copy_path, \
"/opt/sensor-test/apps/")
        #run test get sensor by id and show it's information
        fp = os.path.join(os.path.dirname(__file__), "sensor_id.json")
        jsf = json.load(file(fp))
        cmd = "/opt/sensor-test/apps/test_switch_get_sensor_data"
        client_cmd = "%s %s %s"%(cmd, jsf[0], jsf[1])
        print client_cmd
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 1, msg="Error messages: %s" % output)   
      def testSwitchGetSensorDataNegative(self):
        '''Verify sensor data can be got after trying to connect an invalid sensor'''
        #Prepare test binaries to image        
        mkdir_path = "mkdir -p /opt/sensor-test/apps/"
        (status, output) = self.target.run(mkdir_path)
        copy_path = os.path.join(get_files_dir(), 'test_switch_get_sensor_data_negative')
        (status, output) = self.target.copy_to(copy_path, \
"/opt/sensor-test/apps/")
        #run test get sensor by id and show it's information
        fp = os.path.join(os.path.dirname(__file__), "sensor_id.json")
        jsf = json.load(file(fp))
        fp = os.path.join(os.path.dirname(__file__), "invalid_sensor_id.json")
        jsf2 = json.load(file(fp))
        cmd = "/opt/sensor-test/apps/test_switch_get_sensor_data_negative"
        client_cmd = "%s %s %s"%(cmd, jsf[0], jsf2[0])
        print client_cmd
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 1, msg="Error messages: %s" % output) 
