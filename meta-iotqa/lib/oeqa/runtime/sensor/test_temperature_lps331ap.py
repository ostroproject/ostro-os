"""
@file test_temperature_lps331ap.py
"""
##
# @addtogroup soletta sensor
# @brief This is sensor test based on soletta app
# @brief test temperature function of sensor lps331ap on Galileo/MinnowMax

import os
import time
from oeqa.utils.helper import shell_cmd
from oeqa.oetest import oeRuntimeTest
from oeqa.runtime.sensor.EnvirSetup import EnvirSetup
from oeqa.utils.decorators import tag

@tag(TestType="FVT", FeatureID="IOTOS-757")
class TestTemperatureLPS331AP(oeRuntimeTest):
    """
    @class TestTemperatureLPS331AP
    """
    def setUp(self):
        '''Generate test app on target
        @fn setUp
        @param self
        @return'''
        print ('start!\n')
        #connect sensor and DUT through board
        #shell_cmd("sudo python "+ os.path.dirname(__file__) + "/Connector.py lps331ap")
        envir = EnvirSetup(self.target)
        envir.envirSetup("lps331ap","temperature")

    def tearDown(self):
        '''unload lps331ap driver
        @fn tearDown
        @param self
        @return'''
        (status, output) = self.target.run("cat /sys/devices/virtual/dmi/id/board_name")
        if "Minnow" in output:
           (status, output) = self.target.run(
                         "cd /sys/bus/i2c/devices; \
                          echo 0x5d >i2c-1/delete_device")
        if "Galileo" in output:
           (status, output) = self.target.run(
                         "cd /sys/bus/i2c/devices; \
                          echo 0x5d >i2c-0/delete_device")
        
    def test_Temperature_LPS331AP(self):
        '''Execute the test app and verify sensor data
        @fn test_Temperature_LPS331AP
        @param self
        @return'''
        print ('start reading data!')
        (status, output) = self.target.run(
                         "chmod 777 /opt/apps/test_temperature_lps331ap.fbp")
        (status, output) = self.target.run(
                         "cd /opt/apps; ./test_temperature_lps331ap.fbp >re.log")
        (status, output) = self.target.run(
                         "cd /opt/apps; ./test_temperature_lps331ap.fbp >re.log")
        error = output
        (status, output) = self.target.run(
                         "cp /opt/apps/re.log /home/root/lps331ap_temperature.log") 
        #verification of target sensor data
        (status, output) = self.target.run("cat /opt/apps/re.log|grep float")
        print (output + "\n")
        self.assertEqual(status, 0, msg="Error messages: %s" % error) 
        #make sure sensor data is valid 
        (status, output) = self.target.run("cat /opt/apps/re.log|grep ' 0.000000'")
        self.assertEqual(status, 1, msg="Error messages: %s" % output)      
