"""
@file comm_wifi_stability.py
"""

##
# @addtogroup wifi
# @brief This is component
# @{
# @addtogroup comm_wifi_stability
# @brief This is comm_wifi_stability module
# @{
##

import time
import os
import string
from oeqa.runtime.wifi import wifi
try:
 import ConfigParser
except:
 import configparser as ConfigParser
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import shell_cmd_timeout
from oeqa.utils.decorators import tag

ssid_config = ConfigParser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), "files/config.ini")
ssid_config.readfp(open(config_path))

@tag(TestType="EFT")
class CommWiFiStable(oeRuntimeTest):
    """
    @class CommWiFiStable
    """
    def setUp(self):
        ''' initialize wifi class 
        @fn setUp
        @param self
        @return
        '''
        self.wifi = wifi.WiFiFunction(self.target)

    def tearDown(self):
        ''' disable after testing 
        @fn tearDown
        @param self
        @return
        '''
        # disable wifi
        self.wifi.disable_wifi()

    @tag(FeatureID="IOTOS-462")
    def test_wifi_onoff_multiple_time(self):
        '''connmanctl to enable/disable wifi for multiple times
        @fn test_wifi_onoff_multiple_time
        @param self
        @return
        '''
        time=200
        for i in range(1, time):
            self.wifi.enable_wifi()
            self.wifi.disable_wifi()
            if i % 10 == 0:
                print ("Finish %d times, successful." % i)

##
# @}
# @}
##

