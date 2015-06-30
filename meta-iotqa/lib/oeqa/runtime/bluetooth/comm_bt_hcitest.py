import string
import time
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import shell_cmd_timeout

class CommBTHCITest(oeRuntimeTest):
    '''Bluetooth test by hci commands'''
    def test_hciconfig_up(self):
        '''hciconfig enables bluetooth device'''
        # un-block software rfkill lock
        self.target.run('rfkill unblock all')
        # Disable BT firstly
        (status, output) = self.target.run('hciconfig hci0 down')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
        (status, output) = self.target.run('hciconfig | grep DOWN > /dev/null 2>&1')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

        # Enable BT
        (status, output) = self.target.run('hciconfig hci0 up')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
        (status, output) = self.target.run('hciconfig | grep DOWN > /dev/null 2>&1')
        self.assertTrue(
            status != 0,
            msg="Error messages: %s" % output)

    def test_hciconfig_iscan(self):
        '''hciconfig set iscan for visible mode'''
        # un-block software rfkill lock
        self.target.run('rfkill unblock all')
        # Enable BT firstly
        (status, output) = self.target.run('hciconfig hci0 up')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

        # Make iscan
        (status, output) = self.target.run('hciconfig hci0 iscan')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
        (status, output) = self.target.run('hciconfig | grep ISCAN > /dev/null 2>&1')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

    def test_hciconfig_leadv(self):
        '''Do LE advertising, others scan'''
        # un-block software rfkill lock
        self.target.run('rfkill unblock all')
        # Enable BT firstly
        (status, output) = self.target.run('hciconfig hci0 up')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

        # Target does advertising
        (status, Target_MAC) = self.target.run("hciconfig | grep 'BD Address' | awk '{print $3}'")
        (status, output) = self.target.run('hciconfig hci0 leadv')

        # Host do lescan to find such MAC
        ret, output = shell_cmd_timeout('hciconfig hci0 reset', timeout=10)
        cmd = 'hcitool lecc %s' % Target_MAC
        ret, output = shell_cmd_timeout(cmd, timeout=60)
        self.assertEqual(ret, 0, msg="Fail to connect advertising device:\n%s" % Target_MAC)

    def test_hcitool_scan(self):
        '''Use hcitool to scan nearby devices'''
        # un-block software rfkill lock
        self.target.run('rfkill unblock all')
        # Enable BT firstly
        (status, output) = self.target.run('hciconfig hci0 up')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

        # hcitool scan nearby
        (status, output) = self.target.run('hcitool scan | wc -l')
        output_lines = string.atoi(output)
        self.assertTrue(
            output_lines > 1,
            msg="Error messages: %s" % output)

    '''Due to hcitool lescan is unable to print result to a file, comment on this case
    def test_hcitool_lescan(self):
        # un-block software rfkill lock
        self.target.run('rfkill unblock all')
        # Enable BT firstly
        (status, output) = self.target.run('hciconfig hci0 up')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

        # Host does advertising
        cmd = "hciconfig | grep 'BD Address' | awk '{print $3}'"
        ret, host_mac = shell_cmd_timeout(cmd, timeout=10)
        ret, output = shell_cmd_timeout('hciconfig hci0 leadv', timeout=10)

        # Target does lescan to find such MAC
        (status, output) = self.target.run('hciconfig hci0 noleadv')
        (status, output) = self.target.run('hcitool lescan > /tmp/scanlog &')
        time.sleep(20)
        (status, output) = self.target.run('killall hcitool')
        (status, output) = self.target.run('grep %s /tmp/scanlog' % host_mac)
        self.assertEqual(status, 0, msg="Fail to find advertising device:\n%s" % host_mac)
    '''
    def test_hcitool_lecc(self):
        '''Use hcitool lecc to connect remote advertising BLE device'''
        # un-block software rfkill lock
        self.target.run('rfkill unblock all')
        # Enable BT firstly
        (status, output) = self.target.run('hciconfig hci0 up')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

        # Host does advertising
        cmd = "hciconfig | grep 'BD Address' | awk '{print $3}'"
        ret, host_mac = shell_cmd_timeout(cmd, timeout=10)
        ret, output = shell_cmd_timeout('hciconfig hci0 leadv', timeout=10)

        # Target creates the connection to Host
        (status, output) = self.target.run('hciconfig hci0 noleadv')
        (status, output) = self.target.run('hcitool lecc %s' % host_mac)
        self.assertEqual(status, 0, msg="Error messages: %s" % output)


 
