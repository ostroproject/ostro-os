"""
@file test_light_tsl2561.py
"""
##
# @addtogroup soletta sensor
# @brief This is sensor test based on soletta app
# @brief test sensor tsl2561 on Galileo/MinnowMax/Edison
##

import os
import time
from oeqa.utils.helper import shell_cmd
from oeqa.oetest import oeRuntimeTest
from oeqa.runtime.sensor.EnvirSetup import EnvirSetup
from oeqa.utils.decorators import tag

@tag(TestType="FVT", FeatureID="IOTOS-757")
class TestLightTsl2561(oeRuntimeTest):
    """
    @class TestLightTsl2561
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
        
    def tearDown(self):
        '''unload tsl2561 driver
        @fn tearDown
        @param self
        @return'''
        (status, output) = self.target.run("cat /sys/devices/virtual/dmi/id/board_name")
        if "Minnow" in output:
           (status, output) = self.target.run(
                         "cd /sys/bus/i2c/devices; \
                          echo 0x39 >i2c-1/delete_device")
        elif "Galileo" in output or "SDS" in output:
           (status, output) = self.target.run(
                         "cd /sys/bus/i2c/devices; \
                          echo 0x39 >i2c-0/delete_device")
        elif "BODEGA" in output:
           (status, output) = self.target.run(
                         "cd /sys/bus/i2c/devices; \
                          echo 0x39 >i2c-6/delete_device")
    def test_Light_TSL2561(self):
        '''Execute the test app and verify sensor data
        @fn testLightTSL2561
        @param self
        @return'''
        print ('start reading data!')
        (status, output) = self.target.run(
                         "chmod 777 /opt/apps/test_light_tsl2561.fbp")
        (status, output) = self.target.run(
                          "cd /opt/apps; ./test_light_tsl2561.fbp >re.log")
        error = output 
        (status, output) = self.target.run(
                         "cp /opt/apps/re.log /home/root/tsl2561.log") 
        #verification of target sensor data
        (status, output) = self.target.run("cat /opt/apps/re.log|grep float")
        print (output + "\n")
        self.assertEqual(status, 0, msg="Error messages: %s" % error) 
        #make sure sensor data is valid 
        (status, output) = self.target.run("cat /opt/apps/re.log|grep ' 0.000000'")
        self.assertEqual(status, 1, msg="Error messages: %s" % output)      
