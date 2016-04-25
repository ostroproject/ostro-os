"""
@file test_color_tcs3414cs.py
"""
##
# @addtogroup soletta sensor
# @brief This is sensor test based on soletta app
# @brief test sensor tcs3414cs on Galileo/MinnowMax
##

import os
import time
from oeqa.utils.helper import shell_cmd
from oeqa.oetest import oeRuntimeTest
from EnvirSetup import EnvirSetup
from oeqa.utils.decorators import tag

@tag(TestType="FVT", FeatureID="IOTOS-757")
class TestColorTcs3414CS(oeRuntimeTest):
    """
    @class TestColorTcs3414CS
    """
    def setUp(self):
        '''Generate test app on target
        @fn setUp
        @param self
        @return'''
        print 'start!\n'
        #connect sensor and DUT through board
        #shell_cmd("sudo python "+ os.path.dirname(__file__) + "/Connector.py tcs3414cs")
        envir = EnvirSetup(self.target)
        envir.envirSetup("tcs3414cs","color")
        
    def tearDown(self):
        '''unload tcs3414cs driver
        @fn tearDown
        @param self
        @return'''
        (status, output) = self.target.run("cat /sys/devices/virtual/dmi/id/board_name")
        if "Minnow" in output:
           (status, output) = self.target.run(
                         "cd /sys/bus/i2c/devices; \
                          echo 0x39 >i2c-1/delete_device")
        if "Galileo" in output:
           (status, output) = self.target.run(
                         "cd /sys/bus/i2c/devices; \
                          echo 0x39 >i2c-0/delete_device")

    def test_Color_Tcs3414cs(self):
        '''Execute the test app and verify sensor data
        @fn test_Color_Tcs3414cs
        @param self
        @return'''
        print 'start reading data!'
        (status, output) = self.target.run(
                         "chmod 777 /opt/apps/test_color_tcs3414cs.fbp")
        (status, output) = self.target.run(
                         "cd /opt/apps; ./test_color_tcs3414cs.fbp >re.log")
        error = output 
        (status, output) = self.target.run(
                         "cp /opt/apps/re.log /home/root/tcs3414cs.log") 
        #verification of target sensor data
        (status, output) = self.target.run("cat /opt/apps/re.log|grep rgb")
        print output + "\n"
        self.assertEqual(status, 0, msg="Error messages: %s" % error) 
