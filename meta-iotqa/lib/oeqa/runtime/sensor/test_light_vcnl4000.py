"""
@file test_light_vcnl4000.py
"""
##
# @addtogroup soletta sensor
# @brief This is sensor test based on soletta app
# @brief test sensor vcnl4000 on Galileo/MinnowMax/Edison
##

import os
import time
from oeqa.utils.helper import shell_cmd
from oeqa.oetest import oeRuntimeTest
from EnvirSetup import EnvirSetup
from oeqa.utils.decorators import tag

@tag(TestType="FVT", FeatureID="IOTOS-757")
class TestLightVcnl4000(oeRuntimeTest):
    """
    @class TestLightVcnl4000
    """
    def setUp(self):
        '''Generate test app on target
        @fn setUp
        @param self
        @return'''
        print 'start!\n'
        #connect sensor and DUT through board
        #shell_cmd("sudo python "+ os.path.dirname(__file__) + "/Connector.py vcnl4000")
        envir = EnvirSetup(self.target)
        envir.envirSetup("vcnl4000","light")
        
    def tearDown(self):
        '''unload vcnl4000 driver
        @fn tearDown
        @param self
        @return'''
        (status, output) = self.target.run("cat /sys/devices/virtual/dmi/id/board_name")
        if "Minnow" in output:
           (status, output) = self.target.run(
                         "cd /sys/bus/i2c/devices; \
                          echo 0x13 >i2c-1/delete_device")
        if "Galileo" in output:
           (status, output) = self.target.run(
                         "cd /sys/bus/i2c/devices; \
                          echo 0x13 >i2c-0/delete_device")
        if "BODEGA" in output:
           (status, output) = self.target.run(
                         "cd /sys/bus/i2c/devices; \
                          echo 0x13 >i2c-6/delete_device")

    def test_Light_VCNL4000(self):
        '''Execute the test app and verify sensor data
        @fn testLightVCNL4000
        @param self
        @return'''
        print 'start reading data!'
        (status, output) = self.target.run(
                         "chmod 777 /opt/apps/test_light_vcnl4000.fbp")
        (status, output) = self.target.run(
                         "cd /opt/apps; ./test_light_vcnl4000.fbp >re.log")
        error = output 
        (status, output) = self.target.run(
                         "cp /opt/apps/re.log /home/root/vcnl4000.log") 
        #verification of target sensor data
        (status, output) = self.target.run("cat /opt/apps/re.log|grep float")
        print output + "\n"
        self.assertEqual(status, 0, msg="Error messages: %s" % error) 
        #make sure sensor data is valid 
        (status, output) = self.target.run("cat /opt/apps/re.log|grep ' 0.000000'")
        self.assertEqual(status, 1, msg="Error messages: %s" % output)      
