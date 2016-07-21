"""
@file test_color_isl29125.py
"""
##
# @addtogroup soletta sensor
# @brief This is sensor test based on soletta app
# @brief test sensor isl29125 on Galileo/MinnowMax
##

import os
import time
from oeqa.utils.helper import shell_cmd
from oeqa.oetest import oeRuntimeTest
from oeqa.runtime.sensor.EnvirSetup import EnvirSetup
from oeqa.utils.decorators import tag

@tag(TestType="FVT", FeatureID="IOTOS-757")
class TestColorISL29125(oeRuntimeTest):
    """
    @class TestColorISL29125
    """
    def setUp(self):
        '''Generate test app on target
        @fn setUp
        @param self
        @return'''
        print ('start!\n')
        #connect sensor and DUT through board
        #shell_cmd("sudo python "+ os.path.dirname(__file__) + "/Connector.py isl29125")
        envir = EnvirSetup(self.target)
        envir.envirSetup("isl29125","color")
        
    def tearDown(self):
        '''unload isl29125 driver
        @fn tearDown
        @param self
        @return'''
        (status, output) = self.target.run("cat /sys/devices/virtual/dmi/id/board_name")
        if "Minnow" in output:
           (status, output) = self.target.run(
                         "cd /sys/bus/i2c/devices; \
                          echo 0x44 >i2c-1/delete_device")
        elif "Galileo" in output or "SDS" in output:
           (status, output) = self.target.run(
                         "cd /sys/bus/i2c/devices; \
                          echo 0x44 >i2c-0/delete_device")

    def test_Color_ISL29125(self):
        '''Execute the test app and verify sensor data
        @fn test_Color_ISL29125
        @param self
        @return'''
        print ('start reading data!')
        (status, output) = self.target.run(
                         "chmod 777 /opt/apps/test_color_isl29125.fbp")
        (status, output) = self.target.run(
                         "cd /opt/apps; ./test_color_isl29125.fbp >re.log")
        error = output 
        (status, output) = self.target.run(
                         "cp /opt/apps/re.log /home/root/isl29125.log") 
        #verification of target sensor data
        (status, output) = self.target.run("cat /opt/apps/re.log|grep rgb")
        print (output + "\n")
        self.assertEqual(status, 0, msg="Error messages: %s" % error) 
        #make sure sensor data is valid 
        (status, output) = self.target.run("cat /opt/apps/re.log|grep ' 000, 000, 000'")
        self.assertEqual(status, 1, msg="Error messages: %s" % output)      
