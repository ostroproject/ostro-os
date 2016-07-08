"""
@file test_light_tsl2561_4_hrs.py
"""
##
# @addtogroup soletta sensor
# @brief This is sensor test based on soletta app
# @brief test data reading for 4 hours from sensor tsl2561 on Galileo/MinnowMax/Edison
##

import os
import time
import subprocess
from oeqa.utils.helper import shell_cmd
from oeqa.oetest import oeRuntimeTest
from oeqa.runtime.sensor.EnvirSetup import EnvirSetup
from oeqa.utils.decorators import tag

@tag(TestType="EFT", FeatureID="IOTOS-757")
class TestLightTsl2561FourHrs(oeRuntimeTest):
    """
    @class TestLightTsl2561FourHrs
    """
    def setUp(self):
        '''Generate test app on target
        @fn setUp
        @param self
        @return'''
        print ('start!\n')
        #connect sensor and DUT through board
        #shell_cmd("sudo python "+ os.path.dirname(__file__) + "/Connector.py tsl2561")
        envir = EnvirSetup(self.target)
        envir.envirSetup("tsl2561","light")
        #update fbp file to run the data reading for 4 hrs
        timeUpdate = "sed -i 's/3000/14400000/g' /opt/apps/test_light_tsl2561.fbp" 
        (status, output) = self.target.run(timeUpdate)
        print (output)
        renameTC = "mv /opt/apps/test_light_tsl2561.fbp /opt/apps/test_light_tsl2561_4_hrs.fbp"
        (status, output) = self.target.run(renameTC)

    def tearDown(self):
        '''unload tsl2561 driver
        @fn tearDown
        @param self
        @return'''
        (status, output) = self.target.run(
                         "cd /sys/bus/i2c/devices; \
                          echo 0x39 >i2c-0/delete_device")
        
    def test_read_data_from_tsl2561_for_4_hrs(self):
        '''Execute the test app and verify sensor data
        @fn test_read_data_from_tsl2561_for_4_hrs
        @param self
        @return'''
        print ('start reading data!')
        (status, output) = self.target.run(
                         "chmod 777 /opt/apps/test_light_tsl2561_4_hrs.fbp")        
        (status, output) = self.target.run(
                         "touch /opt/apps/re.log")
        ssh_cmd = "ssh root@%s -o UserKnownHostsFile=/dev/null\
                   -o StrictHostKeyChecking=no -o LogLevel=ERROR" % self.target.ip
        sensor_cmd = "\"cd /opt/apps; ./test_light_tsl2561_4_hrs.fbp >/opt/apps/re.log\""
        p1 = subprocess.Popen("%s %s" % (ssh_cmd, sensor_cmd), shell = True, stderr = subprocess.PIPE)
        time.sleep(10)
        #check data ouput for every 5 minutes and stop if things go wrong
        i = 0
        while i <48:
          (status, output) = self.target.run(
                         "tail /opt/apps/re.log -n 1")
          print ("the output is:%s\n" % output)
          #if no data received, kill the process and print (error log)
          if output == "":
             p1.kill()
             line = p1.stderr.readline()
             self.assertEqual(1, 0, msg="Error messages: %s" % line) 
          #if data received is invalid, kill the process
          if " 0.000000" in output:
             p1.kill()
             break
          else:
             i = i + 1
             time.sleep(300)
        p1.wait()
        #makse sure sensor data is received
        print ("test done\n")
        (status, output) = self.target.run("cat /opt/apps/re.log|grep float")
        self.assertEqual(status, 0, msg="Error messages: %s" % output) 
        #make sure sensor data is valid 
        (status, output) = self.target.run("cat /opt/apps/re.log|grep ' 0.000000'")
        self.assertEqual(status, 1, msg="Error messages: %s" % output)      
