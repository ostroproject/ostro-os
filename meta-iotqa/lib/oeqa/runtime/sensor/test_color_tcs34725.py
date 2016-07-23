"""
@file test_color_tcs34725.py
"""
##
# @addtogroup soletta sensor
# @brief This is sensor test based on soletta app
# @brief test sensor tcs34725 on Galileo/MinnowMax
##

import os
import time
from oeqa.utils.helper import shell_cmd
from oeqa.oetest import oeRuntimeTest
from oeqa.runtime.sensor.EnvirSetup import EnvirSetup
from oeqa.utils.decorators import tag

@tag(TestType="FVT", FeatureID="IOTOS-757")
class TestColorTcs34725(oeRuntimeTest):
    """
    @class TestColorTcs34725
    """
    def setUp(self):
        '''Generate test app on target
        @fn setUp
        @param self
        @return'''
        print ('start!\n')
        #connect sensor and DUT through board
        #shell_cmd("sudo python "+ os.path.dirname(__file__) + "/Connector.py tcs34725")
        envir = EnvirSetup(self.target)
        envir.envirSetup("tcs34725","color")
        
    def tearDown(self):
        '''unload tcs34725 driver
        @fn tearDown
        @param self
        @return'''
        (status, output) = self.target.run("cat /sys/devices/virtual/dmi/id/board_name")
        if "Minnow" in output:
           (status, output) = self.target.run(
                         "cd /sys/bus/i2c/devices; \
                          echo 0x29 >i2c-1/delete_device")
        elif "Galileo" in output or "SDS" in output:
           (status, output) = self.target.run(
                         "cd /sys/bus/i2c/devices; \
                          echo 0x29 >i2c-0/delete_device")

    def test_Color_Tcs34725(self):
        '''Execute the test app and verify sensor data
        @fn test_Color_Tcs34725
        @param self
        @return'''
        print ('start reading data!')
        (status, output) = self.target.run(
                         "chmod 777 /opt/apps/test_color_tcs34725.fbp")
        (status, output) = self.target.run(
                         "cd /opt/apps; ./test_color_tcs34725.fbp >re.log")
        error = output 
        (status, output) = self.target.run(
                         "cp /opt/apps/re.log /home/root/tcs34725.log") 
        #verification of target sensor data
        (status, output) = self.target.run("cat /opt/apps/re.log|grep rgb")
        print (output + "\n")
        self.assertEqual(status, 0, msg="Error messages: %s" % error) 
        #make sure sensor data is valid 
        (status, output) = self.target.run("cat /opt/apps/re.log|grep ' 000, 000, 000'")
        self.assertEqual(status, 1, msg="Error messages: %s" % output)      
