import time
from oeqa.oetest import oeRuntimeTest

class CommWiFiTest(oeRuntimeTest):
    '''WiFi test by connmanctl'''
    def test_wifi_connect_nopassword(self):
        '''connmanctl to connect a no-password wifi AP'''
        # un-block software rfkill lock
        self.target.run('rfkill unblock all')
        # Enable WiFi
        (status, output) = self.target.run('connmanctl enable wifi')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

        # Scan nearby to get service of Guest
        (status, output) = self.target.run('connmanctl scan wifi')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
        (status, services) = self.target.run("connmanctl services | grep Guest | awk '{print $NF}'")
        # will do scan retry 1 time if needed
        if (status != 0):
            (status, output) = self.target.run('connmanctl scan wifi')
            self.assertEqual(status, 0, msg="Error messages: %s" % output)
            (status, services) = self.target.run("connmanctl services | grep Guest | awk '{print $NF}'")
            self.assertEqual(status, 0, msg="Not found AP service for Guest")

        # Do connection
        (status, output) = self.target.run('connmanctl disconnect %s' % services)
        time.sleep(2)
        i = 1
        (status, output) = self.target.run('connmanctl connect %s' % services)
        # will do connection retry 4 times if needed
        while ( 'Connected ' not in output ):
            print("connection retry for the %d time" % i)
            (status, output) = self.target.run('connmanctl connect %s' % services)
            i = i + 1
            if (i == 5):
                break
            
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
        time.sleep(30)

        # Check ip address by ifconfig command
        (status, output) = self.target.run("ifconfig wlp2s0 | grep 'inet addr:'")
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
        

    def tearDown(self):
        ''' disable wifi after testing '''
 
        self.target.run('connmanctl disable wifi')
