import time
import os
import string
import ConfigParser
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import shell_cmd_timeout
from oeqa.utils.helper import get_files_dir
from oeqa.utils.helper import tag

ssid_config = ConfigParser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), "files/config.ini")
ssid_config.readfp(open(config_path))

@tag(TestType="Functional Positive")
class CommWiFiConect(oeRuntimeTest):
    hidden_service = ""
    def setUp(self):
        # un-block software rfkill lock
        self.target.run('rfkill unblock all')
        # Enable WiFi
        (status, output) = self.target.run('connmanctl enable wifi')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
        time.sleep(20)
        # Scan nearby to get service of none-encryption broadcasting ssid
        hidden_str = "hidden_managed_psk"
        (status, output) = self.target.run('connmanctl scan wifi')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
        (status, services) = self.target.run("connmanctl services | grep %s" % hidden_str)
        # will do scan retry 1 time if needed
        if (status != 0):
            (status, output) = self.target.run('connmanctl scan wifi')
            self.assertEqual(status, 0, msg="Error messages: %s" % output)
            (status, services) = self.target.run("connmanctl services | grep %s" % hidden_str)
            self.assertEqual(status, 0, msg="Not found hidden AP service")
        self.hidden_service = services.strip()

    def tearDown(self):
        ''' disable wifi after testing '''
        self.target.run('connmanctl disable wifi')

    @tag(FeatureID="IOTOS-457")
    def test_wifi_connect_80211b(self):
        '''connmanctl to connect 802.11b wifi AP'''
        target_ip = self.target.ip 
        ssid = ssid_config.get("Connect","ssid_80211b")
        pwd = ssid_config.get("Connect","passwd_80211b")

        # Do connection
        exp = os.path.join(os.path.dirname(__file__), "files/wifi_hidden_connect.exp")
        cmd = "expect %s %s %s %s %s %s" % (exp, target_ip, "connmanctl", self.hidden_service, ssid, pwd) 
        status, output = shell_cmd_timeout(cmd, timeout=60)
        self.assertEqual(status, 2, msg="Error messages: %s" % output)
        # Check ip address by ifconfig command
        (status, wifi_interface) = self.target.run("ifconfig | grep '^wlp' | awk '{print $1}'")
        (status, output) = self.target.run("ifconfig %s | grep 'inet addr:'" % wifi_interface)
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

    @tag(FeatureID="IOTOS-457")
    def test_wifi_connect_80211g(self):
        '''connmanctl to connect 802.11g wifi AP'''
        target_ip = self.target.ip 
        ssid = ssid_config.get("Connect","ssid_80211g")
        pwd = ssid_config.get("Connect","passwd_80211g")

        # Do connection
        exp = os.path.join(os.path.dirname(__file__), "files/wifi_hidden_connect.exp")
        cmd = "expect %s %s %s %s %s %s" % (exp, target_ip, "connmanctl", self.hidden_service, ssid, pwd) 
        status, output = shell_cmd_timeout(cmd, timeout=60)
        self.assertEqual(status, 2, msg="Error messages: %s" % output)
        # Check ip address by ifconfig command
        (status, wifi_interface) = self.target.run("ifconfig | grep '^wlp' | awk '{print $1}'")
        (status, output) = self.target.run("ifconfig %s | grep 'inet addr:'" % wifi_interface)
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

    @tag(FeatureID="IOTOS-457")
    def test_wifi_connect_80211n(self):
        '''connmanctl to connect 802.11n wifi AP'''
        target_ip = self.target.ip 
        ssid = ssid_config.get("Connect","ssid_80211n")
        pwd = ssid_config.get("Connect","passwd_80211n")

        # Do connection
        exp = os.path.join(os.path.dirname(__file__), "files/wifi_hidden_connect.exp")
        cmd = "expect %s %s %s %s %s %s" % (exp, target_ip, "connmanctl", self.hidden_service, ssid, pwd) 
        status, output = shell_cmd_timeout(cmd, timeout=60)
        self.assertEqual(status, 2, msg="Error messages: %s" % output)
        # Check ip address by ifconfig command
        (status, wifi_interface) = self.target.run("ifconfig | grep '^wlp' | awk '{print $1}'")
        (status, output) = self.target.run("ifconfig %s | grep 'inet addr:'" % wifi_interface)
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

    @tag(FeatureID="IOTOS-458")
    def test_wifi_connect_wpapsk(self):
        '''connmanctl to connect WPA-PSK wifi AP (set by ssid_80211b AP)'''
        target_ip = self.target.ip 
        ssid = ssid_config.get("Connect","ssid_80211b")
        pwd = ssid_config.get("Connect","passwd_80211b")

        # Do connection
        exp = os.path.join(os.path.dirname(__file__), "files/wifi_hidden_connect.exp")
        cmd = "expect %s %s %s %s %s %s" % (exp, target_ip, "connmanctl", self.hidden_service, ssid, pwd) 
        status, output = shell_cmd_timeout(cmd, timeout=60)
        self.assertEqual(status, 2, msg="Error messages: %s" % output)
        # Check ip address by ifconfig command
        (status, wifi_interface) = self.target.run("ifconfig | grep '^wlp' | awk '{print $1}'")
        (status, output) = self.target.run("ifconfig %s | grep 'inet addr:'" % wifi_interface)
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

    @tag(FeatureID="IOTOS-458")
    def test_wifi_connect_wpa2psk(self):
        '''connmanctl to connect WPA2-PSK wifi AP (set by ssid_80211g AP)'''
        target_ip = self.target.ip 
        ssid = ssid_config.get("Connect","ssid_80211g")
        pwd = ssid_config.get("Connect","passwd_80211g")

        # Do connection
        exp = os.path.join(os.path.dirname(__file__), "files/wifi_hidden_connect.exp")
        cmd = "expect %s %s %s %s %s %s" % (exp, target_ip, "connmanctl", self.hidden_service, ssid, pwd) 
        status, output = shell_cmd_timeout(cmd, timeout=60)
        self.assertEqual(status, 2, msg="Error messages: %s" % output)
        # Check ip address by ifconfig command
        (status, wifi_interface) = self.target.run("ifconfig | grep '^wlp' | awk '{print $1}'")
        (status, output) = self.target.run("ifconfig %s | grep 'inet addr:'" % wifi_interface)
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
