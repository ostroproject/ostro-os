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

@tag(TestType="Functional Positive")
class CommWiFiConect(oeRuntimeTest):
    hidden_service = ""
    def setUp(self):
        # un-block software rfkill lock
        self.target.run('rfkill unblock all')
        # Enable WiFi
        (status, output) = self.target.run('connmanctl enable wifi')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
        time.sleep(30)
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
        ''' disable wifi after testing '''
        self.target.run('connmanctl disable wifi')

    @tag(FeatureID="IOTOS-458")
    def test_wifi_connect(self):
        '''connmanctl to connect WPA2-PSK wifi AP'''
        target_ip = self.target.ip 
        ssid = ssid_config.get("Connect","ssid")
        pwd = ssid_config.get("Connect","passwd")

        # Do connection
        exp = os.path.join(os.path.dirname(__file__), "files/wifi_hidden_connect.exp")
        cmd = "expect %s %s %s %s %s %s" % (exp, target_ip, "connmanctl", self.hidden_service, ssid, pwd) 
        status, output = shell_cmd_timeout(cmd, timeout=60)
        self.assertEqual(status, 2, msg="Error messages: %s" % output)
        # Check ip address by ifconfig command
        time.sleep(3)
        (status, wifi_interface) = self.target.run("ifconfig | grep '^wlp' | awk '{print $1}'")
        (status, output) = self.target.run("ifconfig %s | grep 'inet addr:'" % wifi_interface)
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
