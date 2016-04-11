"""
@file test_adc_ads7955.py
"""
##
# @addtogroup soletta sensor
# @brief This is sensor test based on soletta app
# @brief test adc sensor ads7955 on Galileo
##

import os
import time
from oeqa.utils.helper import shell_cmd
from oeqa.oetest import oeRuntimeTest
from EnvirSetup import EnvirSetup
from oeqa.utils.decorators import tag

@tag(TestType="FVT", FeatureID="IOTOS-757")
class TestAdcADS7955(oeRuntimeTest):
    """
    @class TestAdcADS7955
    """
    def setUp(self):
        '''Generate test app on target
        @fn setUp
        @param self
        @return'''
        print 'start!\n'
        envir = EnvirSetup(self.target)
        envir.envirSetup("ads7955","adc")
        
    def test_Adc_ADS7955(self):
        '''Execute the test app and verify sensor data
        @fn test_Adc_ADS7955
        @param self
        @return'''
        print 'start reading data!'
        (status, output) = self.target.run(
                         "chmod 777 /opt/apps/test_adc_ads7955.fbp")
        (status, output) = self.target.run(
                         "cd /opt/apps; ./test_adc_ads7955.fbp >re.log")
        error = output
        (status, output) = self.target.run(
                         "cp /opt/apps/re.log /home/root/ads7955.log")
        #verification of target sensor data
        (status, output) = self.target.run("cat /opt/apps/re.log|grep float")
        print output + "\n"
        self.assertEqual(status, 0, msg="Error messages: %s" % error)
