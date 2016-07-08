"""
@file test_adc_int3495.py
"""
##
# @addtogroup soletta sensor
# @brief This is sensor test based on soletta app
# @brief test adc sensor int3495 on Galileo
##

import os
import time
from oeqa.utils.helper import shell_cmd
from oeqa.oetest import oeRuntimeTest
from oeqa.runtime.sensor.EnvirSetup import EnvirSetup
from oeqa.utils.decorators import tag

@tag(TestType="FVT", FeatureID="IOTOS-757")
class TestAdcINT3495(oeRuntimeTest):
    """
    @class TestAdcINT3495
    """
    def setUp(self):
        '''Generate test app on target
        @fn setUp
        @param self
        @return'''
        print ('start!\n')
        envir = EnvirSetup(self.target)
        envir.envirSetup("int3495","adc")
        
    def test_Adc_INT3495(self):
        '''Execute the test app and verify sensor data
        @fn test_Adc_INT3495
        @param self
        @return'''
        print ('start reading data!')
        (status, output) = self.target.run(
                         "chmod 777 /opt/apps/test_adc_int3495.fbp")
        (status, output) = self.target.run(
                         "cd /opt/apps; ./test_adc_int3495.fbp >re.log")
        error = output
        (status, output) = self.target.run(
                         "cp /opt/apps/re.log /home/root/int3495.log")
        #verification of target sensor data
        (status, output) = self.target.run("cat /opt/apps/re.log|grep float")
        print (output + "\n")
        self.assertEqual(status, 0, msg="Error messages: %s" % error)
