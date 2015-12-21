"""
@file comm_wifi_connect_7260.py
"""

##
# @addtogroup sanity sanity
# @brief This is sanity component
# @{
# @addtogroup comm_wifi_connect_7260 comm_wifi_connect_7260
# @brief This is comm_wifi_connect_7260 module
# @{
##

import time
import os
import string
import ConfigParser
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import shell_cmd_timeout
from oeqa.utils.decorators import tag

ssid_config = ConfigParser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), "files/config.ini")
ssid_config.readfp(open(config_path))

@tag(TestType="Functional Positive")
class CommWiFiConect(oeRuntimeTest):
    """
    @class CommWiFiConect
    """
    service = ""
    log = ""
    def target_collect_info(self, cmd):
        """
        @fn target_collect_info
        @param self
        @param  cmd
        @return
        """
        (status, output) = self.target.run(cmd)
        self.log = self.log + "\n\n[Debug] Command output --- %s: \n" % cmd
        self.log = self.log + output

    def setUp(self):
        """
        @fn setUp
        @param self
        @return
        """
        # un-block software rfkill lock
        self.target.run('rfkill unblock all')
        # Enable WiFi
        self.target.run('connmanctl disable wifi')
        time.sleep(1)
        (status, output) = self.target.run('connmanctl enable wifi')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
        time.sleep(30)
        m_type = ssid_config.get("Connect","type")
        if (m_type == "broadcast"):
            ssid = ssid_config.get("Connect","ssid")
            # For broadcast AP, get its service firstly.
            retry = 0
            while (retry < 4):
                self.target.run('connmanctl disable wifi')
                time.sleep(1)
                self.target.run('connmanctl enable wifi')
                time.sleep(1)
                (status, output) = self.target.run('connmanctl scan wifi')
                self.assertEqual(status, 0, msg="Error messages: %s" % output)
                (status, output) = self.target.run("connmanctl services | grep %s" % ssid)
                retry = retry + 1
                if (status == 0):
                    break
                else:
                    self.target_collect_info("connmanctl services")
            # Collect info
            self.target_collect_info("ifconfig")
            self.assertEqual(status, 0, msg="Not found AP service" + self.log)
            self.service = output.split(" ")[-1]
        else:
            # Scan nearby to get service of none-encryption broadcasting ssid
            hidden_str = "hidden_managed_psk"
            # will do scan retry 3 times if needed
            retry = 0
            while (retry < 4):
                self.target.run('connmanctl disable wifi')
                time.sleep(1)
                self.target.run('connmanctl enable wifi')
                time.sleep(1)
                (status, output) = self.target.run('connmanctl scan wifi')
                self.assertEqual(status, 0, msg="Error messages: %s" % output)
                (status, services) = self.target.run("connmanctl services | grep %s" % hidden_str)
                retry = retry + 1
                if (status == 0):
                    break
                else:
                    self.target_collect_info("connmanctl services")
            # Collect info
            self.target_collect_info("ifconfig")
            self.assertEqual(status, 0, msg="Not found hidden AP service" + self.log)
            self.service = services.strip()

    def tearDown(self):
        ''' disable wifi after testing 
        @fn tearDown
        @param self
        @return
        '''
        self.target.run('connmanctl disable wifi')

    @tag(FeatureID="IOTOS-458")
    def test_wifi_connect(self):
        '''connmanctl to connect WPA2-PSK wifi AP
        @fn test_wifi_connect
        @param self
        @return
        '''
        target_ip = self.target.ip 
        ssid = ssid_config.get("Connect","ssid")
        pwd = ssid_config.get("Connect","passwd")

        # Do connection
        m_type = ssid_config.get("Connect","type")
        if (m_type == "broadcast"):
            exp = os.path.join(os.path.dirname(__file__), "files/wifi_connect_7260.exp")
            cmd = "expect %s %s %s %s %s" % (exp, target_ip, "connmanctl", self.service, pwd)
        else:
            exp = os.path.join(os.path.dirname(__file__), "files/wifi_hidden_connect_7260.exp")
            cmd = "expect %s %s %s %s %s %s" % (exp, target_ip, "connmanctl", self.service, ssid, pwd)
        status, output = shell_cmd_timeout(cmd, timeout=60)
        ##
        # TESTPOINT: #1, test_wifi_connect
        #
        self.assertEqual(status, 2, msg="Error messages: %s" % output)
        # Check ip address by ifconfig command
        time.sleep(3)
        (status, wifi_interface) = self.target.run("ifconfig | grep '^wlp' | awk '{print $1}'")
        (status, output) = self.target.run("ifconfig %s | grep 'inet addr:'" % wifi_interface)

        # Collect info
        self.target_collect_info("ifconfig")
        ##
        # TESTPOINT: #2, test_wifi_connect
        #
        self.assertEqual(status, 0, msg="IP check failed" + self.log)

##
# @}
# @}
##

