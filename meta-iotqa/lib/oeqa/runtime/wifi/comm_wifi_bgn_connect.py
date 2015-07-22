import time
import os
import ConfigParser
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import get_files_dir

ssid_config = ConfigParser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), "config.ini")
ssid_config.readfp(open(config_path))

class CommWiFiBGNConect(oeRuntimeTest):
    def test_wifi_connect_80211b(self):
        '''connmanctl to connect a no-password 802.11b wifi AP'''
        ssid = ssid_config.get("Connect","ssid_80211b")

        # un-block software rfkill lock
        self.target.run('rfkill unblock all')
        # Enable WiFi
        (status, output) = self.target.run('connmanctl enable wifi')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
        time.sleep(3)

        # Scan nearby to get service of Guest
        (status, output) = self.target.run('connmanctl scan wifi')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
        (status, services) = self.target.run("connmanctl services | grep %s | awk '{print $NF}'" % ssid)
        self.assertEqual(status, 0, msg="Not found AP service for %s" % ssid)

        # Do connection
        (status, output) = self.target.run('connmanctl disconnect %s' % services)
        time.sleep(2)
        i = 0
        (status, output) = self.target.run('connmanctl connect %s' % services)
        while ( 'Connected ' not in output ):
            (status, output) = self.target.run('connmanctl connect %s' % services)
            i = i + 1
            if (i == 4):
                break
            
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
        time.sleep(15)

        # Check ip address by ifconfig command
        (status, output) = self.target.run("ifconfig wlp2s0 | grep 'inet addr:'")
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
        
    def test_wifi_connect_80211g(self):
        '''connmanctl to connect a no-password 802.11g wifi AP'''
        ssid = ssid_config.get("Connect","ssid_80211g")

        # un-block software rfkill lock
        self.target.run('rfkill unblock all')
        # Enable WiFi
        (status, output) = self.target.run('connmanctl enable wifi')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
        time.sleep(3)

        # Scan nearby to get service of Guest
        (status, output) = self.target.run('connmanctl scan wifi')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
        (status, services) = self.target.run("connmanctl services | grep %s | awk '{print $NF}'" % ssid)
        self.assertEqual(status, 0, msg="Not found AP service for %s" % ssid)

        # Do connection
        (status, output) = self.target.run('connmanctl disconnect %s' % services)
        time.sleep(2)
        i = 0
        (status, output) = self.target.run('connmanctl connect %s' % services)
        while ( 'Connected ' not in output ):
            (status, output) = self.target.run('connmanctl connect %s' % services)
            i = i + 1
            if (i == 4):
                break
            
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
        time.sleep(15)

        # Check ip address by ifconfig command
        (status, output) = self.target.run("ifconfig wlp2s0 | grep 'inet addr:'")
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
        
    def test_wifi_connect_80211n(self):
        '''connmanctl to connect a no-password 802.11n wifi AP'''
        ssid = ssid_config.get("Connect","ssid_80211n")

        # un-block software rfkill lock
        self.target.run('rfkill unblock all')
        # Enable WiFi
        (status, output) = self.target.run('connmanctl enable wifi')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
        time.sleep(3)

        # Scan nearby to get service of Guest
        (status, output) = self.target.run('connmanctl scan wifi')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
        (status, services) = self.target.run("connmanctl services | grep %s | awk '{print $NF}'" % ssid)
        self.assertEqual(status, 0, msg="Not found AP service for %s" % ssid)

        # Do connection
        (status, output) = self.target.run('connmanctl disconnect %s' % services)
        time.sleep(2)
        i = 0
        (status, output) = self.target.run('connmanctl connect %s' % services)
        while ( 'Connected ' not in output ):
            (status, output) = self.target.run('connmanctl connect %s' % services)
            i = i + 1
            if (i == 4):
                break
            
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
        time.sleep(15)

        # Check ip address by ifconfig command
        (status, output) = self.target.run("ifconfig wlp2s0 | grep 'inet addr:'")
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

    def tearDown(self):
        ''' disable wifi after testing '''

        self.target.run('connmanctl disable wifi')
 
