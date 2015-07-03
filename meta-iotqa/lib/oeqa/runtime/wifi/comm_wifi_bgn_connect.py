import time
from oeqa.oetest import oeRuntimeTest

class CommWiFiBGNConect(oeRuntimeTest):
    def test_wifi_connect_80211b(self):
        '''connmanctl to connect a no-password 802.11b wifi AP'''
        ssid="shz14f-ssgotcqalab-ap01-iot"
        # un-block software rfkill lock
        self.target.run('rfkill unblock all')
        # Enable WiFi
        (status, output) = self.target.run('connmanctl enable wifi')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

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
        '''connmanctl to connect a no-password 802.11b wifi AP'''
        ssid="shz14f-ssgotcqalab-ap02-iot"
        # un-block software rfkill lock
        self.target.run('rfkill unblock all')
        # Enable WiFi
        (status, output) = self.target.run('connmanctl enable wifi')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

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
        '''connmanctl to connect a no-password 802.11b wifi AP'''
        ssid="shz13-otc-bsp-tests"
        # un-block software rfkill lock
        self.target.run('rfkill unblock all')
        # Enable WiFi
        (status, output) = self.target.run('connmanctl enable wifi')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

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
        
