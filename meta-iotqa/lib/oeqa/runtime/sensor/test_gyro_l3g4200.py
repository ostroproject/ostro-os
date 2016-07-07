"""
@file test_gyro_l3g4200.py
"""
##
# @addtogroup soletta sensor
# @brief This is sensor test based on soletta app
# @brief test sensor l3g4200 on Galileo/MinnowMax/Edison
##
import os
import time
from oeqa.utils.helper import shell_cmd
from oeqa.oetest import oeRuntimeTest
from oeqa.runtime.sensor.EnvirSetup import EnvirSetup
from oeqa.utils.decorators import tag

@tag(TestType="FVT", FeatureID="IOTOS-757")
class TestGyroL3G4200(oeRuntimeTest):
    """
    @class TestGyroL3G4200
    """
    def setUp(self):
        '''Generate fbp file on target
        @fn setUp
        @param self
        @return'''
        print ('start!\n')
        #connect sensor and DUT through board
        #shell_cmd("sudo python "+ os.path.dirname(__file__) + "/Connector.py l3g4200")
        envir = EnvirSetup(self.target)
        envir.envirSetup("l3g4200","gyro")

    def tearDown(self):
        '''unload l3g4200 driver
        @fn tearDown
        @param self
        @return'''
        (status, output) = self.target.run("cat /sys/devices/virtual/dmi/id/board_name")
        if "Minnow" in output:
           (status, output) = self.target.run(
                         "cd /sys/bus/i2c/devices; \
                          echo 0x69 >i2c-1/delete_device")
        if "Galileo" in output:
           (status, output) = self.target.run(
                         "cd /sys/bus/i2c/devices; \
                          echo 0x69 >i2c-0/delete_device")
        if "BODEGA" in output:
           (status, output) = self.target.run(
                         "cd /sys/bus/i2c/devices; \
                          echo 0x69 >i2c-6/delete_device")
        
    def test_Gyro_L3G4200(self):
        '''Execute the test app and verify sensor data
        @fn test_Gyro_L3G4200
        @param self
        @return'''
        print ('start reading data!')
        (status, output) = self.target.run(
                         "chmod 777 /opt/apps/test_gyro_l3g4200.fbp")
        (status, output) = self.target.run(
                         "cd /opt/apps; ./test_gyro_l3g4200.fbp >re.log")        
        error = output
        (status, output) = self.target.run(
                         "cp /opt/apps/re.log /home/root/l3g4200.log")         
        (status, output) = self.target.run("cat /opt/apps/re.log|grep direction-vector")
        print (output + "\n")
        self.assertEqual(status, 0, msg="Error messages: %s" % error) 
        #make sure sensor data is valid 
        (status, output) = self.target.run("cat /opt/apps/re.log|grep '0.000000, 0.000000, 0.000000'")
        self.assertEqual(status, 1, msg="Error messages: %s" % output)      
