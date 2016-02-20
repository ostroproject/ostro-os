"""
@file iotvt_wifi.py
"""

##
# @addtogroup iotivity iotivity
# @brief This is iotivity component
# @{
# @addtogroup iotvt_wifi iotvt_wifi
# @brief This is iotvt_wifi module
# @{
##

import os
import time
import string
import ConfigParser
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import shell_cmd_timeout
from oeqa.utils.decorators import tag

ssid_config = ConfigParser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), "../sanity/files/config.ini")
ssid_config.readfp(open(config_path))

@tag(TestType="FVT", FeatureID="IOTOS-499")
class IOtvtWiFi(oeRuntimeTest):
    """
    @class IOtvtWiFi
    """
    @classmethod
    def setUpClass(cls):
        '''Connect to WiFi AP, which contains simpleserver running on it
        @fn setUpClass
        @param cls
        @return
        '''
        # Connect to WiFi
        cls.tc.target.run('rfkill unblock all')
        cls.tc.target.run('connmanctl enable wifi')
        time.sleep(20)

        target_ip = cls.tc.target.ip
        m_type = ssid_config.get("Connect","type")
        ssid = ssid_config.get("Connect","ssid")
        pwd = ssid_config.get("Connect","passwd")
        service = "nothing"
        if (m_type == "broadcast"):
            # For broadcast AP, get its service firstly.
            retry = 0
            while (retry < 4):
                (status, output) = cls.tc.target.run('connmanctl scan wifi')
                (status, output) = cls.tc.target.run("connmanctl services | grep %s" % ssid)
                retry = retry + 1
                if (status == 0):
                    break
            assert status == 0, "Not found AP service"
            service = output.split(" ")[-1]
            exp = os.path.join(os.path.dirname(__file__), "../sanity/files/wifi_connect.exp")
            cmd = "expect %s %s %s %s %s" % (exp, target_ip, "connmanctl", service, pwd)
        else:
            # Scan nearby to get service of none-encryption broadcasting ssid
            hidden_str = "hidden_managed_psk"
            retry = 0
            while (retry < 4):
                (status, output) = cls.tc.target.run('connmanctl scan wifi')
                (status, output) = cls.tc.target.run("connmanctl services | grep %s" % hidden_str)
                retry = retry + 1
                if (status == 0):
                    break
            assert status == 0, "Not found hidden AP service"
            service = output.strip()
            exp = os.path.join(os.path.dirname(__file__), "../sanity/files/wifi_hidden_connect.exp")
            cmd = "expect %s %s %s %s %s %s" % (exp, target_ip, "connmanctl", service, ssid, pwd)

        status, output = shell_cmd_timeout(cmd, timeout=60)
        assert status == 2, "Error messages: %s" % output
        time.sleep(3)
        (status, wifi_interface) = cls.tc.target.run("ifconfig | grep '^wlp|^wlan' | awk '{print $1}'")
        (status, output) = cls.tc.target.run("ifconfig %s | grep 'inet addr:'" % wifi_interface)
        assert status == 0, "No wifi IP address"
        
        # Clean up all iotivity related daemons
        cls.tc.target.run("killall presenceserver presenceclient devicediscoveryserver devicediscoveryclient")        
        cls.tc.target.run("killall fridgeserver fridgeclient garageserver garageclient groupserver groupclient")
        cls.tc.target.run("killall roomserver roomclient simpleserver simpleclient simpleserverHQ simpleclientHQ")
        cls.tc.target.run("killall simpleclientserver threadingsample")
        # Do simpleclient test
        client_cmd = "/opt/iotivity/examples/resource/cpp/simpleclient > /tmp/output &"
        cls.tc.target.run(client_cmd)
        print "\npatient... simpleclient needs long time for its observation"
        time.sleep(70)

    @classmethod
    def tearDownClass(cls):
        '''disable wifi, it will block ethernet connection when rebooting
        @fn tearDownClass
        @param cls
        @return
        '''
        cls.tc.target.run("connmanctl disable wifi")

    def test_iotvt_wifi_findresource(self):
        '''Target finds resource, registered by Host
        @fn test_iotvt_wifi_findresource
        @param self
        @return
        '''
        (status, output) = self.target.run('cat /tmp/output')
        ret = 0
        if "DISCOVERED Resource" in output:
            pass
        else:
           ret = 1
        ##
        # TESTPOINT: #1, test_iotvt_wifi_findresource
        #
        self.assertEqual(ret, 0, msg="Error messages: %s" % output)

    def test_iotvt_wifi_getstate(self):
        '''Target gets resource state
        @fn test_iotvt_wifi_getstate
        @param self
        @return
        '''
        (status, output) = self.target.run('cat /tmp/output')
        ret = 0
        if "GET request was successful" in output:
            pass
        else:
           ret = 1
        ##
        # TESTPOINT: #1, test_iotvt_wifi_getstate
        #
        self.assertEqual(ret, 0, msg="Error messages: %s" % output)

    def test_iotvt_wifi_observer(self):
        '''Target sets observer
        @fn test_iotvt_wifi_observer
        @param self
        @return
        '''
        (status, output) = self.target.run('cat /tmp/output')
        ret = 0
        if "Observe is used." in output:
            pass
        else:
           ret = 1
        ##
        # TESTPOINT: #1, test_iotvt_wifi_observer
        #
        self.assertEqual(ret, 0, msg="Error messages: %s" % output)

    def test_iotvt_wifi_setstate(self):
        '''Target sets resource state
        @fn test_iotvt_wifi_setstate
        @param self
        @return
        '''
        (status, output) = self.target.run('cat /tmp/output')
        ret = 0
        if "PUT request was successful" in output:
            pass
        else:
           ret = 1
        ##
        # TESTPOINT: #1, test_iotvt_wifi_setstate
        #
        self.assertEqual(ret, 0, msg="Error messages: %s" % output)

##
# @}
# @}
##

