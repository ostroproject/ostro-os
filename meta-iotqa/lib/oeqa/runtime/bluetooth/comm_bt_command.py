"""
@file comm_bt_command.py
"""

##
# @addtogroup bluetooth bluetooth
# @brief This is bluetooth component
# @{
# @addtogroup comm_bt_command comm_bt_command
# @brief This is comm_bt_command module
# @{
##

import os
import time
import subprocess
import bluetooth
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import shell_cmd_timeout
from oeqa.utils.helper import get_files_dir
from oeqa.utils.decorators import tag

@tag(TestType="FVT")
class CommBTTest(oeRuntimeTest):
    """
    @class CommBTTest
    """
    def setUp(self):
        """
        @fn setUp
        @param self
        @return
        """
        self.bt = bluetooth.BTFunction(self.target)
        self.bt.target_hciconfig_init()
        self.bt.host_hciconfig_init()

        (status, output) = self.target.run('which gatttool')
        if (status != 0):
            copy_to_path = os.path.join(get_files_dir(), 'gatttool')
            (status, output) = self.target.copy_to(copy_to_path, "/usr/bin/")

    @tag(FeatureID="IOTOS-453")
    def test_bt_pairing(self):
        '''Use bluetoothctl to pair IoT device with host
        @fn test_bt_pairing
        @param self
        @return
        '''
        # On IoT target, start pair_slave in back-ground 
        (status, host_btmac) = shell_cmd_timeout("hciconfig | grep 'BD Address' | awk '{print $3}'")
        slave_exp = os.path.join(os.path.dirname(__file__), "files/bt_pair_slave_on_iot.exp")
        cmd = "%s %s %s" % (slave_exp, self.target.ip, host_btmac)
        subprocess.Popen(cmd, shell=True)
 
        # On Host, get to know target BT mac and perform pair_master
        master_exp = os.path.join(os.path.dirname(__file__), "files/bt_pair_master.exp")
        (status, target_btmac) = self.target.run("hciconfig | grep 'BD Address' | awk '{print $3}'")
        cmd = "expect %s %s" % (master_exp, target_btmac)
        status, output = shell_cmd_timeout(cmd, timeout=200)
        ##
        # TESTPOINT: #1, test_bt_pairing
        #
        self.assertEqual(status, 2, msg="expect excution fail: %s" % output)

        # On Host, check paired devices to see if IoT is in
        check_exp = os.path.join(os.path.dirname(__file__), "files/bt_list_paired_device.exp")
        status, output = shell_cmd_timeout("%s | grep '^Device %s'" % (check_exp, target_btmac), timeout=200)
        ##
        # TESTPOINT: #2, test_bt_pairing
        #
        self.assertEqual(status, 0, msg="Not found IoT device paired")

    @tag(FeatureID="IOTOS-456")
    def test_bt_gatt_read_primary(self):
        '''Use gatttool to show target primary attr handles
        @fn test_bt_gatt_read_primary
        @param self
        @return
        '''
        # On target, do LE advertising
        self.target.run('hciconfig hci0 leadv')
        time.sleep(1)
        # Host does gatttool commands
        (status, target_btmac) = self.target.run("hciconfig | grep 'BD Address' | awk '{print $3}'")
        cmd = "gatttool -b %s --primary | grep '^attr handle'" % target_btmac
        status, output = shell_cmd_timeout(cmd, timeout=200)
        ##
        # TESTPOINT: #1, test_bt_gatt_read_primary
        #
        self.assertEqual(status, 0, msg="Primary info is wrong")

    @tag(FeatureID="IOTOS-456")
    def test_bt_gatt_read_characteristics(self):
        '''Use gatttool to show target characteristics handles
        @fn test_bt_gatt_read_characteristics
        @param self
        @return
        '''
        # On target, do LE advertising
        self.target.run('hciconfig hci0 leadv')
        time.sleep(1)
        # Host does gatttool commands
        (status, target_btmac) = self.target.run("hciconfig | grep 'BD Address' | awk '{print $3}'")
        cmd = "gatttool -b %s --characteristics | grep '^handle'" % target_btmac
        status, output = shell_cmd_timeout(cmd, timeout=200)
        ##
        # TESTPOINT: #1, test_bt_gatt_read_characteristics
        #
        self.assertEqual(status, 0, msg="characteristics info is wrong")

    @tag(FeatureID="IOTOS-456")
    def test_bt_gatt_read_handle(self):
        '''Use gatttool to read target handle value
        @fn test_bt_gatt_read_handle
        @param self
        @return
        '''
        # On target, do LE advertising
        self.target.run('hciconfig hci0 leadv')
        time.sleep(1)
        # Host does gatttool commands
        (status, target_btmac) = self.target.run("hciconfig | grep 'BD Address' | awk '{print $3}'")
        cmd = "gatttool -b %s --char-read -a 0x0002 | grep '02 03 00 00 2a'" % target_btmac
        status, output = shell_cmd_timeout(cmd, timeout=200)
        ##
        # TESTPOINT: #1, test_bt_gatt_read_handle
        #
        self.assertEqual(status, 0, msg="handle 0x0002 value is wrong")

    @tag(FeatureID="IOTOS-456")
    def test_bt_gatt_connect(self):
        '''Use gatttool interactive mode to do connect
        @fn test_bt_gatt_connect
        @param self
        @return
        '''
        # On target, do LE advertising
        self.target.run('hciconfig hci0 leadv')
        time.sleep(1)
        # Host does gatttool commands
        (status, target_btmac) = self.target.run("hciconfig | grep 'BD Address' | awk '{print $3}'")
        connect_exp = os.path.join(os.path.dirname(__file__), "files/gatt_connect.exp")
        cmd = "expect %s %s" % (connect_exp, target_btmac)
        status, output = shell_cmd_timeout(cmd, timeout=200)
        ##
        # TESTPOINT: #1, test_bt_gatt_connect
        #
        self.assertEqual(status, 2, msg="gatttool connect target fails: %s" % output) 

    @tag(FeatureID="IOTOS-453")
    def test_bt_power_on(self):
        '''enable bluetooth device
        @fn test_bt_power_on
        @param self
        @return
        '''
        self.target.run('hciconfig hci0 down')
        self.bt.ctl_power_on()

    @tag(FeatureID="IOTOS-453")
    def test_bt_power_off(self):
        '''disable bluetooth device
        @fn test_bt_power_off
        @param self
        @return
        '''
        self.target.run('hciconfig hci0 up')
        self.bt.ctl_power_off()

    @tag(FeatureID="IOTOS-453")
    def test_bt_visable_on(self):
        '''enable visibility
        @fn test_bt_visable_on
        @param self
        @return
        '''
        self.target.run('hciconfig hci0 noscan')
        self.bt.ctl_visable_on()

    @tag(FeatureID="IOTOS-453")
    def test_bt_visable_off(self):
        '''disable visibility
        @fn test_bt_visable_off
        @param self
        @return
        '''
        self.target.run('hciconfig hci0 piscan')
        self.bt.ctl_visable_off()

    @tag(FeatureID="IOTOS-456")
    def test_bt_visible_scan(self):
        '''Scan nearby bluetooth devices (not ble scan)
        @fn test_bt_visible_scan
        @param self
        @return
        '''
        # Close target's leadv
        self.target.run('hciconfig hci0 noleadv')
        self.target.run('hciconfig hci0 piscan')
        time.sleep(1)
        (status, target_btmac) = self.target.run("hciconfig | grep 'BD Address' | awk '{print $3}'")
        # start bluetoothctl to scan target 
        exp = os.path.join(os.path.dirname(__file__), "files/bt_scan.exp")
        cmd = "expect %s %s" % (exp, target_btmac)
        status, output = shell_cmd_timeout(cmd, timeout=100)
        shell_cmd_timeout('hciconfig hci0 reset', timeout=100)
        self.target.run('hciconfig hci0 reset')
        ##
        # TESTPOINT: #1, test_bt_visible_scan
        #
        self.assertEqual(status, 2, msg="scan target fails: %s" % output) 

    @tag(FeatureID="IOTOS-759")
    def test_bt_leadv(self):
        '''Target does LE advertising, Host scan target
        @fn test_bt_leadv
        @param self
        @return
        '''
        # close target piscan firstly, and then enable leadv
        self.target.run('hciconfig hci0 leadv')
        time.sleep(1)
        (status, target_btmac) = self.target.run("hciconfig | grep 'BD Address' | awk '{print $3}'")
        # start bluetoothctl to scan target 
        exp = os.path.join(os.path.dirname(__file__), "files/bt_lescan.exp")
        cmd = "expect %s %s" % (exp, target_btmac)
        status, output = shell_cmd_timeout(cmd, timeout=100)
        shell_cmd_timeout('hciconfig hci0 reset', timeout=100)
        self.target.run('hciconfig hci0 reset')
        ##
        # TESTPOINT: #1, test_bt_leadv
        #
        self.assertEqual(status, 2, msg="scan target leadv fails: %s" % output) 

    @tag(FeatureID="IOTOS-770")
    def test_bt_le_scan(self):
        '''Another device (host) does LE advertising, target scan
        @fn test_bt_le_scan
        @param self
        @return
        '''
        # close host piscan firstly, and then enable leadv
        status, output = shell_cmd_timeout('hciconfig hci0 leadv 3', timeout=100)
        time.sleep(1)
        (status, host_btmac) = shell_cmd_timeout("hciconfig | grep 'BD Address' | awk '{print $3}'", timeout=100)
        # From target, start bluetoothctl to scan host
        exp = os.path.join(os.path.dirname(__file__), "files/bt_target_lescan.exp")
        cmd = "expect %s %s %s" % (exp, self.target.ip, host_btmac)
        status, output = shell_cmd_timeout(cmd, timeout=100)
        shell_cmd_timeout('hciconfig hci0 reset', timeout=100)
        self.target.run('hciconfig hci0 reset')
        ##
        # TESTPOINT: #1, test_bt_le_scan
        #
        self.assertEqual(status, 2, msg="scan host leadv fails: %s" % output) 

    @tag(FeatureID="IOTOS-456")
    def test_bt_target_gatt_read_primary(self):
        '''Use gatttool to show host primary attr handles
        @fn test_bt_target_gatt_read_primary
        @param self
        @return
        '''
        # On Host, do LE advertising
        shell_cmd_timeout('hciconfig hci0 leadv')
        time.sleep(1)
        # Target does gatttool commands
        (status, host_btmac) = shell_cmd_timeout("hciconfig | grep 'BD Address' | awk '{print $3}'")
        cmd = "gatttool --primary -b %s | grep '^attr handle'" % host_btmac.strip("\n")
        status, output = self.target.run(cmd, timeout=200)
        ##
        # TESTPOINT: #1, test_bt_target_gatt_read_primary
        #
        self.assertEqual(status, 0, msg="Host primary info is wrong")

    @tag(FeatureID="IOTOS-456")
    def test_bt_target_gatt_read_characteristics(self):
        '''Use gatttool to show host characteristics handles
        @fn test_bt_target_gatt_read_characteristics
        @param self
        @return
        '''
        # On host, do LE advertising
        shell_cmd_timeout('hciconfig hci0 leadv')
        time.sleep(1)
        # Target does gatttool commands
        (status, host_btmac) = shell_cmd_timeout("hciconfig | grep 'BD Address' | awk '{print $3}'")
        cmd = "gatttool --characteristics -b %s | grep '^handle'" % host_btmac.strip("\n")
        status, output = self.target.run(cmd, timeout=200)
        ##
        # TESTPOINT: #1, test_bt_target_gatt_read_characteristics
        #
        self.assertEqual(status, 0, msg="Host characteristics info is wrong")

    @tag(FeatureID="IOTOS-456")
    def test_bt_target_gatt_read_handle(self):
        '''Use gatttool to read host handle value
        @fn test_bt_target_gatt_read_handle
        @param self
        @return
        '''
        # On target, do LE advertising
        shell_cmd_timeout('hciconfig hci0 leadv')
        time.sleep(1)
        # Target does gatttool commands
        (status, host_btmac) = shell_cmd_timeout("hciconfig | grep 'BD Address' | awk '{print $3}'")
        print host_btmac
        cmd = "gatttool --char-read -a 0x0002 -b %s | grep '02 03 00 00 2a'" % host_btmac.strip("\n")
        print cmd
        status, output = self.target.run(cmd, timeout=200)
        ##
        # TESTPOINT: #1, test_bt_target_gatt_read_handle
        #
        self.assertEqual(status, 0, msg="Host handle 0x0002 value is wrong")

    @tag(FeatureID="IOTOS-456")
    def test_bt_target_gatt_connect(self):
        '''Use gatttool interactive mode to do connect to host
        @fn test_bt_target_gatt_connect
        @param self
        @return
        '''
        # On target, do LE advertising
        shell_cmd_timeout('hciconfig hci0 leadv')
        time.sleep(1)
        # Target does gatttool commands
        (status, host_btmac) = shell_cmd_timeout("hciconfig | grep 'BD Address' | awk '{print $3}'")
        connect_exp = os.path.join(os.path.dirname(__file__), "files/gatt_connect_target.exp")
        cmd = "expect %s %s %s" % (connect_exp, self.target.ip, host_btmac)
        status, output = shell_cmd_timeout(cmd, timeout=200)
        ##
        # TESTPOINT: #1, test_bt_target_gatt_connect
        #
        self.assertEqual(status, 2, msg="gatttool connect host fails: %s" % output) 

##
# @}
# @}
##

