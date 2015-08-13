import os
import subprocess
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import shell_cmd_timeout
from oeqa.utils.helper import get_files_dir
from oeqa.utils.helper import tag

@tag(TestType="Functional Positive")
class CommBTTest(oeRuntimeTest):
    def setUp(self):
        # un-block software rfkill lock
        self.target.run('rfkill unblock all')
        self.target.run('hciconfig hci0 up')
        self.target.run('hciconfig hci0 piscan')
        status, output = shell_cmd_timeout('hciconfig hci0 up', timeout=200)
        status, output = shell_cmd_timeout('hciconfig hci0 piscan', timeout=200)

    @tag(FeatureID="IOTOS-453")
    def test_bt_pairing(self):
        '''Use bluetoothctl to pair IoT device with host'''
        # On IoT target, start pair_slave in back-ground 
        slave_exp = os.path.join(os.path.dirname(__file__), "files/bt_pair_slave_on_iot.exp")
        cmd = "%s %s" % (slave_exp, self.target.ip)
        subprocess.Popen(cmd, shell=True)
 
        # On Host, get to know target BT mac and perform pair_master
        master_exp = os.path.join(os.path.dirname(__file__), "files/bt_pair_master.exp")
        (status, target_btmac) = self.target.run("hciconfig | grep 'BD Address' | awk '{print $3}'")
        cmd = "%s %s" % (master_exp, target_btmac)
        status, output = shell_cmd_timeout(cmd, timeout=200)

        # On Host, check paired devices to see if IoT is in
        check_exp = os.path.join(os.path.dirname(__file__), "files/bt_list_paired_device.exp")
        status, output = shell_cmd_timeout("%s | grep '^Device %s'" % (check_exp, target_btmac), timeout=200)
        self.assertEqual(status, 0, msg="Not found IoT device paired")

    @tag(FeatureID="IOTOS-456")
    def test_bt_gatt_read_primary(self):
        '''Use gatttool to show target primary attr handles'''
        # On target, do LE advertising
        self.target.run('hciconfig hci0 leadv')
        # Host does gatttool commands
        (status, target_btmac) = self.target.run("hciconfig | grep 'BD Address' | awk '{print $3}'")
        cmd = "gatttool -b %s --primary | grep '^attr handle'" % target_btmac
        status, output = shell_cmd_timeout(cmd, timeout=200)
        self.assertEqual(status, 0, msg="Primary info is wrong")

    @tag(FeatureID="IOTOS-456")
    def test_bt_gatt_read_characteristics(self):
        '''Use gatttool to show target characteristics handles'''
        # On target, do LE advertising
        self.target.run('hciconfig hci0 leadv')
        # Host does gatttool commands
        (status, target_btmac) = self.target.run("hciconfig | grep 'BD Address' | awk '{print $3}'")
        cmd = "gatttool -b %s --characteristics | grep '^handle'" % target_btmac
        status, output = shell_cmd_timeout(cmd, timeout=200)
        self.assertEqual(status, 0, msg="characteristics info is wrong")

    @tag(FeatureID="IOTOS-456")
    def test_bt_gatt_read_handle(self):
        '''Use gatttool to read target handle value'''
        # On target, do LE advertising
        self.target.run('hciconfig hci0 leadv')
        # Host does gatttool commands
        (status, target_btmac) = self.target.run("hciconfig | grep 'BD Address' | awk '{print $3}'")
        cmd = "gatttool -b %s --char-read -a 0x0002 | grep '02 03 00 00 2a'" % target_btmac
        status, output = shell_cmd_timeout(cmd, timeout=200)
        self.assertEqual(status, 0, msg="handle 0x0002 value is wrong")

    @tag(FeatureID="IOTOS-456")
    def test_bt_gatt_connect(self):
        '''Use gatttool interactive mode to do connect'''
        # On target, do LE advertising
        self.target.run('hciconfig hci0 leadv')
        # Host does gatttool commands
        (status, target_btmac) = self.target.run("hciconfig | grep 'BD Address' | awk '{print $3}'")
        connect_exp = os.path.join(os.path.dirname(__file__), "files/gatt_connect.exp")
        cmd = "%s %s" % (connect_exp, target_btmac)
        status, output = shell_cmd_timeout(cmd, timeout=200)
        if ("CON" in output):
            print "connect succeeds"
            return 0
        else:
            print "connect fails"
            return 1
