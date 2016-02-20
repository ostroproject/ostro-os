"""
@file comm_wifi_connect.py
"""

##
# @addtogroup wifi wifi
# @brief This is wifi component
# @{
# @addtogroup comm_wifi_connect comm_wifi_connect
# @brief This is comm_wifi_connect module
# @{
##

import time
import os
import string
import ConfigParser
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import shell_cmd_timeout
from oeqa.utils.helper import get_files_dir
from oeqa.utils.decorators import tag

ssid_config = ConfigParser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), "files/config.ini")
ssid_config.readfp(open(config_path))

@tag(TestType="FVT")
class CommWiFiConect(oeRuntimeTest):
    """
    @class CommWiFiConect
    """
    hidden_service = ""
    def setUp(self):
        """
        @fn setUp
        @param self
        @return
        """
        # un-block software rfkill lock
        self.target.run('rfkill unblock all')
        # Enable WiFi
        (status, output) = self.target.run('connmanctl enable wifi')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
        time.sleep(20)
        # Scan nearby to get service of none-encryption broadcasting ssid
        hidden_str = "hidden_managed_psk"
        # will do scan retry 3 times if needed
        retry = 0
        while (retry < 4):
            (status, output) = self.target.run('connmanctl scan wifi')
            self.assertEqual(status, 0, msg="Error messages: %s" % output)
            (status, services) = self.target.run("connmanctl services | grep %s" % hidden_str)
            retry = retry + 1
            if (status == 0):
                break
        self.assertEqual(status, 0, msg="Not found hidden AP service")
        self.hidden_service = services.strip()

    def tearDown(self):
        ''' disable wifi after testing 
        @fn tearDown
        @param self
        @return
        '''
        self.target.run('connmanctl disable wifi')

    def check_wifi_ip(self):
        """
        @fn check_wifi_ip
        @param self
        @return
        """
        time.sleep(3)
        # Check ip address by ifconfig command
        wifi_interface = "nothing"
        (status, wifi_interface) = self.target.run("ifconfig | grep '^wlp\|^wlan' | awk '{print $1}'")
        (status, output) = self.target.run("ifconfig %s | grep 'inet addr:'" % wifi_interface)
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

    @tag(FeatureID="IOTOS-457")
    def test_wifi_connect_80211b(self):
        '''connmanctl to connect 802.11b wifi AP
        @fn test_wifi_connect_80211b
        @param self
        @return
        '''
        target_ip = self.target.ip 
        ssid = ssid_config.get("Connect","ssid_80211b")
        pwd = ssid_config.get("Connect","passwd_80211b")

        # Do connection
        exp = os.path.join(os.path.dirname(__file__), "files/wifi_hidden_connect.exp")
        cmd = "expect %s %s %s %s %s %s" % (exp, target_ip, "connmanctl", self.hidden_service, ssid, pwd) 
        status, output = shell_cmd_timeout(cmd, timeout=60)
        ##
        # TESTPOINT: #1, test_wifi_connect_80211b
        #
        self.assertEqual(status, 2, msg="Error messages: %s" % output)
        self.check_wifi_ip()

    @tag(FeatureID="IOTOS-457")
    def test_wifi_connect_80211g(self):
        '''connmanctl to connect 802.11g wifi AP
        @fn test_wifi_connect_80211g
        @param self
        @return
        '''
        target_ip = self.target.ip 
        ssid = ssid_config.get("Connect","ssid_80211g")
        pwd = ssid_config.get("Connect","passwd_80211g")

        # Do connection
        exp = os.path.join(os.path.dirname(__file__), "files/wifi_hidden_connect.exp")
        cmd = "expect %s %s %s %s %s %s" % (exp, target_ip, "connmanctl", self.hidden_service, ssid, pwd) 
        status, output = shell_cmd_timeout(cmd, timeout=60)
        ##
        # TESTPOINT: #1, test_wifi_connect_80211g
        #
        self.assertEqual(status, 2, msg="Error messages: %s" % output)
        self.check_wifi_ip()

    @tag(FeatureID="IOTOS-457")
    def test_wifi_connect_80211n(self):
        '''connmanctl to connect 802.11n wifi AP
        @fn test_wifi_connect_80211n
        @param self
        @return
        '''
        target_ip = self.target.ip 
        ssid = ssid_config.get("Connect","ssid_80211n")
        pwd = ssid_config.get("Connect","passwd_80211n")

        # Do connection
        exp = os.path.join(os.path.dirname(__file__), "files/wifi_hidden_connect.exp")
        cmd = "expect %s %s %s %s %s %s" % (exp, target_ip, "connmanctl", self.hidden_service, ssid, pwd) 
        status, output = shell_cmd_timeout(cmd, timeout=60)
        ##
        # TESTPOINT: #1, test_wifi_connect_80211n
        #
        self.assertEqual(status, 2, msg="Error messages: %s" % output)
        self.check_wifi_ip()

    @tag(FeatureID="IOTOS-458")
    def test_wifi_connect_wpapsk(self):
        '''connmanctl to connect WPA-PSK wifi AP (set by ssid_80211b AP)
        @fn test_wifi_connect_wpapsk
        @param self
        @return
        '''
        target_ip = self.target.ip 
        ssid = ssid_config.get("Connect","ssid_80211b")
        pwd = ssid_config.get("Connect","passwd_80211b")

        # Do connection
        exp = os.path.join(os.path.dirname(__file__), "files/wifi_hidden_connect.exp")
        cmd = "expect %s %s %s %s %s %s" % (exp, target_ip, "connmanctl", self.hidden_service, ssid, pwd) 
        status, output = shell_cmd_timeout(cmd, timeout=60)
        ##
        # TESTPOINT: #1, test_wifi_connect_wpapsk
        #
        self.assertEqual(status, 2, msg="Error messages: %s" % output)
        self.check_wifi_ip()

    @tag(FeatureID="IOTOS-458")
    def test_wifi_connect_wpa2psk(self):
        '''connmanctl to connect WPA2-PSK wifi AP (set by ssid_80211g AP)
        @fn test_wifi_connect_wpa2psk
        @param self
        @return
        '''
        target_ip = self.target.ip 
        ssid = ssid_config.get("Connect","ssid_80211g")
        pwd = ssid_config.get("Connect","passwd_80211g")

        # Do connection
        exp = os.path.join(os.path.dirname(__file__), "files/wifi_hidden_connect.exp")
        cmd = "expect %s %s %s %s %s %s" % (exp, target_ip, "connmanctl", self.hidden_service, ssid, pwd) 
        status, output = shell_cmd_timeout(cmd, timeout=60)
        ##
        # TESTPOINT: #1, test_wifi_connect_wpa2psk
        #
        self.assertEqual(status, 2, msg="Error messages: %s" % output)
        self.check_wifi_ip()

    @tag(FeatureID="IOTOS-490")
    def test_wifi_connect_wpa2psk_broadcast(self):
        '''connmanctl to connect WPA2-PSK wifi AP (not hidden)
        @fn test_wifi_connect_wpa2psk_broadcast
        @param self
        @return
        '''
        target_ip = self.target.ip 
        ssid = ssid_config.get("Connect","ssid_broadcast")
        pwd = ssid_config.get("Connect","passwd_broadcast")

        # For broadcast AP, get its service firstly.
        retry = 0
        while (retry < 4):
            (status, output) = self.target.run('connmanctl scan wifi')
            ##
            # TESTPOINT: #1, test_wifi_connect_wpa2psk_broadcast
            #
            self.assertEqual(status, 0, msg="Error messages: %s" % output)
            (status, output) = self.target.run("connmanctl services | grep %s" % ssid)
            retry = retry + 1
            if (status == 0):
                break
        ##
        # TESTPOINT: #2, test_wifi_connect_wpa2psk_broadcast
        #
        self.assertEqual(status, 0, msg="Not found AP service")
        service = output.split(" ")[-1] 

        # Do connection
        exp = os.path.join(os.path.dirname(__file__), "files/wifi_connect.exp")
        cmd = "expect %s %s %s %s %s" % (exp, target_ip, "connmanctl", service, pwd) 
        status, output = shell_cmd_timeout(cmd, timeout=200)
        ##
        # TESTPOINT: #3, test_wifi_connect_wpa2psk_broadcast
        #
        self.assertEqual(status, 2, msg="Error messages: %s" % output)
        self.check_wifi_ip()

    @tag(FeatureID="IOTOS-528")
    def test_wifi_connect_internet(self):
        '''connmanctl to connect to internet, by broadcast wifi AP
        @fn test_wifi_connect_internet
        @param self
        @return
        '''
        target_ip = self.target.ip 
        ssid = ssid_config.get("Connect","ssid_broadcast")
        pwd = ssid_config.get("Connect","passwd_broadcast")

        # For broadcast AP, get its service firstly.
        retry = 0
        while (retry < 4):
            (status, output) = self.target.run('connmanctl scan wifi')
            ##
            # TESTPOINT: #1, test_wifi_connect_internet
            #
            self.assertEqual(status, 0, msg="Error messages: %s" % output)
            (status, output) = self.target.run("connmanctl services | grep %s" % ssid)
            retry = retry + 1
            if (status == 0):
                break
        ##
        # TESTPOINT: #2, test_wifi_connect_internet
        #
        self.assertEqual(status, 0, msg="Not found AP service")
        service = output.split(" ")[-1] 

        # Do connection
        exp = os.path.join(os.path.dirname(__file__), "files/wifi_connect.exp")
        cmd = "expect %s %s %s %s %s" % (exp, target_ip, "connmanctl", service, pwd) 
        status, output = shell_cmd_timeout(cmd, timeout=200)
        ##
        # TESTPOINT: #3, test_wifi_connect_internet
        #
        self.assertEqual(status, 2, msg="Error messages: %s" % output)
        self.check_wifi_ip()

        # Ping internet web links
        (status, output) = self.target.run("wget http://www.baidu.com")
        ##
        # TESTPOINT: #4, test_wifi_connect_internet
        #
        self.assertEqual(status, 0, msg="Error messages: %s" % output) 

##
# @}
# @}
##

