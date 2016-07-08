"""
@file test_temperature_mpl115.py
"""
##
# @addtogroup soletta sensor
# @brief This is sensor test based on soletta app
# @brief test temperature function of sensor mpl115 on Galileo/MinnowMax

import os
import time
from oeqa.utils.helper import shell_cmd
from oeqa.oetest import oeRuntimeTest
from oeqa.runtime.sensor.EnvirSetup import EnvirSetup
from oeqa.utils.decorators import tag

@tag(TestType="FVT", FeatureID="IOTOS-757")
class TestTemperatureMPL115(oeRuntimeTest):
    """
    @class TestTemperatureMPL115
    """
    def setUp(self):
        '''Generate test app on target
        @fn setUp
        @param self
        @return'''
        print ('start!\n')
        #connect sensor and DUT through board
        #shell_cmd("sudo python "+ os.path.dirname(__file__) + "/Connector.py mpl115")
        envir = EnvirSetup(self.target)
        envir.envirSetup("mpl115","temperature")

    def tearDown(self):
        '''unload mpl115 driver
        @fn tearDown
        @param self
        @return'''
        (status, output) = self.target.run("cat /sys/devices/virtual/dmi/id/board_name")
        if "Minnow" in output:
           (status, output) = self.target.run(
                         "cd /sys/bus/i2c/devices; \
                          echo 0x60 >i2c-1/delete_device")
        if "Galileo" in output:
           (status, output) = self.target.run(
                         "cd /sys/bus/i2c/devices; \
                          echo 0x60 >i2c-0/delete_device")
        
    def test_Temperature_MPL115(self):
        '''Execute the test app and verify sensor data
        @fn test_Temperature_MPL115
        @param self
        @return'''
        print ('start reading data!')
        (status, output) = self.target.run(
                         "chmod 777 /opt/apps/test_temperature_mpl115.fbp")
        (status, output) = self.target.run(
                         "cd /opt/apps; ./test_temperature_mpl115.fbp >re.log")
        error = output
        (status, output) = self.target.run(
                         "cp /opt/apps/re.log /home/root/mpl115_temperature.log") 
        #verification of target sensor data
        (status, output) = self.target.run("cat /opt/apps/re.log|grep float")
        print (output + "\n")
        self.assertEqual(status, 0, msg="Error messages: %s" % error) 
        #make sure sensor data is valid 
        (status, output) = self.target.run("cat /opt/apps/re.log|grep ' 0.000000'")
        self.assertEqual(status, 1, msg="Error messages: %s" % output)      
