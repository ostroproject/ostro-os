"""
@file test_accel_lis3dh.py
"""
##
# @addtogroup soletta sensor
# @brief This is sensor test based on soletta app
# @brief test sensor lis3dh on Galileo/MinnowMax
##

import os
import time
from oeqa.utils.helper import shell_cmd
from oeqa.oetest import oeRuntimeTest
from oeqa.runtime.sensor.EnvirSetup import EnvirSetup
from oeqa.utils.decorators import tag

@tag(TestType="FVT", FeatureID="IOTOS-757")
class TestAccelLIS3DH(oeRuntimeTest):
    """
    @class TestAccelLIS3DH
    """
    def setUp(self):
        '''Generate test app on target
        @fn setUp
        @param self
        @return'''
        print ('start!\n')
        #connect sensor and DUT through board
        #shell_cmd("sudo python "+ os.path.dirname(__file__) + "/Connector.py lis3dh")
        envir = EnvirSetup(self.target)
        envir.envirSetup("lis3dh","accel")

    def tearDown(self):
        '''unload lis3dh driver
        @fn tearDown
        @param self
        @return'''
        (status, output) = self.target.run("cat /sys/devices/virtual/dmi/id/board_name")
        if "Minnow" in output:
           (status, output) = self.target.run(
                         "cd /sys/bus/i2c/devices; \
                          echo 0x19 >i2c-1/delete_device")
        if "Galileo" in output:
           (status, output) = self.target.run(
                         "cd /sys/bus/i2c/devices; \
                          echo 0x19 >i2c-0/delete_device")
        
    def test_Accel_LIS3DH(self):
        '''Execute the test app and verify sensor data
        @fn test_Accel_LIS3DH
        @param self
        @return'''
        print ('start reading data!')
        (status, output) = self.target.run(
                         "chmod 777 /opt/apps/test_accel_lis3dh.fbp")
        (status, output) = self.target.run(
                         "cd /opt/apps; ./test_accel_lis3dh.fbp >re.log")
        error = output
        #check whether data collected
        (status, output) = self.target.run(
                         "cp /opt/apps/re.log /home/root/lis3dh.log")         
        (status, output) = self.target.run("cat /opt/apps/re.log|grep direction-vector")
        print (output + "\n")
        self.assertEqual(status, 0, msg="Error messages: %s" % error) 
        #make sure sensor data is valid 
        (status, output) = self.target.run("cat /opt/apps/re.log|grep '0.000000, 0.000000, 0.000000'")
        self.assertEqual(status, 1, msg="Error messages: %s" % output)      
