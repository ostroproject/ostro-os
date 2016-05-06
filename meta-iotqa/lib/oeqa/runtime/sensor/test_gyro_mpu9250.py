"""
@file test_gyro_mpu9250.py
"""
##
# @addtogroup soletta sensor
# @brief This is sensor test based on soletta app
# @brief test sensor mpu9250 on Galileo/MinnowMax/Edison
##
import os
import time
from oeqa.utils.helper import shell_cmd
from oeqa.oetest import oeRuntimeTest
from EnvirSetup import EnvirSetup
from oeqa.utils.decorators import tag

@tag(TestType="FVT", FeatureID="IOTOS-757")
class TestGyroMPU9250(oeRuntimeTest):
    """
    @class TestGyroMPU9250
    """
    def setUp(self):
        '''Generate fbp file on target
        @fn setUp
        @param self
        @return'''
        print 'start!\n'
        #connect sensor and DUT through board
        #shell_cmd("sudo python "+ os.path.dirname(__file__) + "/Connector.py mpu9250")
        envir = EnvirSetup(self.target)
        envir.envirSetup("mpu9250","gyro")

    def tearDown(self):
        '''unload mpu9250 driver
        @fn tearDown
        @param self
        @return'''
        (status, output) = self.target.run("cat /sys/devices/virtual/dmi/id/board_name")
        if "Minnow" in output:
           (status, output) = self.target.run(
                         "rmmod i2c-minnow-mpu6050")
        if "Galileo" in output:
           (status, output) = self.target.run(
                         "rmmod i2c-quark-mpu6050")
        if "BODEGA" in output:
           (status, output) = self.target.run(
                         "rmmod i2c-edison-mpu6050")
        
    def test_Gyro_MPU9250(self):
        '''Execute the test app and verify sensor data
        @fn test_Gyro_MPU9250
        @param self
        @return'''
        print 'start reading data!'
        (status, output) = self.target.run(
                         "chmod 777 /opt/apps/test_gyro_mpu9250.fbp")
        (status, output) = self.target.run(
                         "cd /opt/apps; ./test_gyro_mpu9250.fbp >re.log")        
        error = output
        (status, output) = self.target.run(
                         "cp /opt/apps/re.log /home/root/mpu9250.log")         
        (status, output) = self.target.run("cat /opt/apps/re.log|grep direction-vector")
        print output + "\n"
        self.assertEqual(status, 0, msg="Error messages: %s" % error) 
        #make sure sensor data is valid 
        (status, output) = self.target.run("cat /opt/apps/re.log|grep '0.000000, 0.000000, 0.000000'")
        self.assertEqual(status, 1, msg="Error messages: %s" % output)      
