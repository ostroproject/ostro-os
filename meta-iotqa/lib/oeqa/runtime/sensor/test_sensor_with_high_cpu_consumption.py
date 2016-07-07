"""
@file test_sensor_with_high_cpu_consumption.py
"""
##
# @addtogroup soletta sensor
# @brief This is sensor test based on soletta app
# @brief test tsl2561 data reading when do tar/untar files
# @brief cpu is consumed about ~90%
##
import os
import time
import subprocess
from oeqa.utils.helper import shell_cmd
from oeqa.oetest import oeRuntimeTest
from oeqa.runtime.sensor.EnvirSetup import EnvirSetup
from oeqa.utils.decorators import tag

@tag(TestType="EFT", FeatureID="IOTOS-757")
class TestSensorWithHighCPUConsumption(oeRuntimeTest):
    """
    @class TestSensorWithHighCPUConsumption
    """
    def setUp(self):
        '''Generate test app on target
        @fn setUp
        @param self
        @return'''
        print ('start!\n')
        #connect sensor and DUT through board
        shell_cmd("sudo python "+ os.path.dirname(__file__) + "/Connector.py tsl2561")
        envir = EnvirSetup(self.target)
        envir.envirSetup("tsl2561","light")
        #update fbp file to run the data reading for 60s
        timeUpdate = "sed -i 's/3000/1800000/g' /opt/apps/test_light_tsl2561.fbp" 
        (status, output) = self.target.run(timeUpdate)
        timeUpdate = "sed -i 's/1000/10/g' /opt/apps/test_light_tsl2561.fbp" 
        (status, output) = self.target.run(timeUpdate)
        copy_to_path = os.path.join(os.path.dirname(__file__) + '/config/powerDiablo')
        (status, output) = self.target.copy_to(copy_to_path, \
                          "/opt/")
        
    def tearDown(self):
        '''unload tsl2561 driver
        @fn tearDown
        @param self
        @return'''
        (status, output) = self.target.run(
                         "cd /sys/bus/i2c/devices; \
                          echo 0x39 >i2c-0/delete_device")

    def test_read_data_from_sensor_with_high_cpu_consumption(self):
        '''Execute the test app and verify sensor data
           at the same time, do tar/untar big files
        @fn test_read_data_from_sensor_with_high_cpu_consumption
        @param self
        @return'''
        (status, output) = self.target.run(
                         "chmod 777 /opt/apps/test_light_tsl2561.fbp")
        (status, output) = self.target.run(
                         "chmod 777 /opt/powerDiablo")
        (status, output) = self.target.run(
                         "touch /opt/apps/re.log")
        (status, output) = self.target.run(
                         "touch /opt/cpu.log")
        ssh_cmd = "ssh root@%s -o UserKnownHostsFile=/dev/null\
                   -o StrictHostKeyChecking=no -o LogLevel=ERROR" % self.target.ip
        sensor_cmd = "\"cd /opt/apps; ./test_light_tsl2561.fbp >/opt/apps/re.log 2>/dev/null\""
        workload_cmd = "\"/opt/powerDiablo -c 100 -t 1800 >/opt/cpu.log\""
        print ("process 1 kicked")
        subprocess.Popen("%s %s" % (ssh_cmd, sensor_cmd), shell=True)
        print ("process 2 kicked")
        subprocess.Popen("%s %s" % (ssh_cmd, workload_cmd), shell=True)
        print ("done\n")
        time.sleep(1800)
        print ("sleep done\n")
        #makse sure sensor data is received
        (status, output) = self.target.run("cat /opt/apps/re.log|grep float")
        self.assertEqual(status, 0, msg="Error messages: %s" % output) 
        #make sure sensor data is valid 
        (status, output) = self.target.run("cat /opt/apps/re.log|grep ' 0.000000'")
        self.assertEqual(status, 1, msg="Error messages: %s" % output)
