"""
@file test_light_bh1750.py
"""
##
# @addtogroup soletta sensor
# @brief This is sensor test based on soletta app
# @brief test sensor bh1750 on Galileo/MinnowMax
##

import os
import time
from oeqa.utils.helper import shell_cmd
from oeqa.oetest import oeRuntimeTest
from oeqa.runtime.sensor.EnvirSetup import EnvirSetup
from oeqa.utils.decorators import tag

@tag(TestType="FVT", FeatureID="IOTOS-757")
class TestLightBH1750(oeRuntimeTest):
    """
    @class TestLightBH1750
    """
    def setUp(self):
        '''Generate test app on target
        @fn setUp
        @param self
        @return'''
        print ('start!\n')
        #connect sensor and DUT through board
        #shell_cmd("sudo python "+ os.path.dirname(__file__) + "/Connector.py bh1750")
        envir = EnvirSetup(self.target)
        envir.envirSetup("bh1750","light")
        
    def tearDown(self):
        '''unload bh1750 driver
        @fn tearDown
        @param self
        @return'''
        (status, output) = self.target.run("cat /sys/devices/virtual/dmi/id/board_name")
        if "Minnow" in output:
           (status, output) = self.target.run(
                         "cd /sys/bus/i2c/devices; \
                          echo 0x23 >i2c-1/delete_device")
        elif "Galileo" in output or "SDS" in output:
           (status, output) = self.target.run(
                         "cd /sys/bus/i2c/devices; \
                          echo 0x23 >i2c-0/delete_device")

    def test_Light_BH1750(self):
        '''Execute the test app and verify sensor data
        @fn test_Light_BH1750
        @param self
        @return'''
        print ('start reading data!')
        (status, output) = self.target.run(
                         "chmod 777 /opt/apps/test_light_bh1750.fbp")
        (status, output) = self.target.run(
                         "cd /opt/apps; ./test_light_bh1750.fbp >re.log")
        error = output 
        (status, output) = self.target.run(
                         "cp /opt/apps/re.log /home/root/bh1750.log") 
        #verification of target sensor data
        (status, output) = self.target.run("cat /opt/apps/re.log|grep float")
        print (output + "\n")
        self.assertEqual(status, 0, msg="Error messages: %s" % error) 
        #make sure sensor data is valid 
        (status, output) = self.target.run("cat /opt/apps/re.log|grep ' 0.000000'")
        self.assertEqual(status, 1, msg="Error messages: %s" % output)      
