"""
@file bluetooth.py
"""

##
# @addtogroup library
# @brief This is library
# @{
# @addtogroup comm_bluetooth
# @brief This is comm_bluetooth module
# @{
##

import time
import os
import string
from oeqa.utils.helper import shell_cmd_timeout

class BTFunction(object):
    """
    @class BTFunction
    """
    log = ""
    def __init__(self, target):
        self.target = target
        # un-block software rfkill lock
        self.target.run('rfkill unblock all')

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

    def target_hciconfig_init(self):
        ''' init target bluetooth by hciconfig commands 
        @fn target_hciconfig_init
        @param self
        @return
        '''
        self.target.run('hciconfig hci0 reset')
        time.sleep(1)
        self.target.run('hciconfig hci0 up')
        self.target.run('hciconfig hci0 piscan')
        self.target.run('hciconfig hci0 noleadv')
        time.sleep(1)

    def host_hciconfig_init(self):
        ''' init host bluetooth by hciconfig commands 
        @fn host_hciconfig_init
        @param self
        @return
        '''
        shell_cmd_timeout('hciconfig hci0 reset', timeout=200)
        time.sleep(1)
        shell_cmd_timeout('hciconfig hci0 up', timeout=100)
        shell_cmd_timeout('hciconfig hci0 piscan', timeout=100)
        shell_cmd_timeout('hciconfig hci0 noleadv', timeout=100)
        time.sleep(1)

    def enable_bluetooth(self):
        ''' enable bluetooth after testing 
        @fn enable_bluetooth
        @param self
        @return
        '''
        # Enable Bluetooth
        (status, output) = self.target.run('connmanctl enable bluetooth')
        assert status == 0, "Error messages: %s" % output 
        time.sleep(1)

    def disable_bluetooth(self):
        ''' disable bluetooth after testing 
        @fn disable_bluetooth
        @param self
        @return
        '''
        (status, output) = self.target.run('connmanctl disable bluetooth')
        assert status == 0, "Error messages: %s" % output 
        # sleep some seconds to ensure disable is done
        time.sleep(1)

    def ctl_power_on(self):
        '''bluetoothctl power on bluetooth device
        @fn ctl_power_on
        @param self
        @return
        '''
        # start bluetoothctl, then input 'power on'
        exp = os.path.join(os.path.dirname(__file__), "files/power_on.exp")
        target_ip = self.target.ip
        status, output = shell_cmd_timeout('expect %s %s' % (exp, target_ip), timeout=200)
        assert status == 2, "power on command fails: %s" % output

    def ctl_power_off(self):
        '''bluetoothctl power off bluetooth device
        @fn ctl_power_off
        @param self
        @return
        '''
        # start bluetoothctl, then input 'power off'
        exp = os.path.join(os.path.dirname(__file__), "files/power_off.exp")
        target_ip = self.target.ip
        status, output = shell_cmd_timeout('expect %s %s' % (exp, target_ip), timeout=200)
        assert status == 2, "power off command fails: %s" % output

    def ctl_visable_on(self):
        '''bluetoothctl enable visibility
        @fn ctl_visable_on
        @param self
        @return
        '''
        # start bluetoothctl, then input 'discoverable on'
        exp = os.path.join(os.path.dirname(__file__), "files/discoverable_on.exp")
        target_ip = self.target.ip
        status, output = shell_cmd_timeout('expect %s %s' % (exp, target_ip), timeout=200)
        assert status == 2, "discoverable on command fails: %s" % output

    def ctl_visable_off(self):
        '''bluetoothctl disable visibility
        @fn ctl_visable_off
        @param self
        @return
        '''
        # start bluetoothctl, then input 'discoverable off'
        exp = os.path.join(os.path.dirname(__file__), "files/discoverable_off.exp")
        target_ip = self.target.ip
        status, output = shell_cmd_timeout('expect %s %s' % (exp, target_ip), timeout=200)
        assert status == 2, "discoverable off command fails: %s" % output

    def insert_6lowpan_module(self):
        '''Insert BLE 6lowpan module
        @fn insert_6lowpan_module
        @param self
        @return
        '''
        status, output = self.target.run('modprobe bluetooth_6lowpan')
        assert status == 0, "insert ble 6lowpan module fail: %s" % output
        # check lsmod, to see if the module is in
        status, output = self.target.run('lsmod')
        if "bluetooth_6lowpan" in output:
            pass
        else:
            target_collect_info('lsmod')
            assert False, "BLE 6lowpan module insert fails. %s" % self.log       

    def enable_6lowpan_ble(self):
        '''Enable 6lowpan over BLE
        @fn enable_6lowpan_ble
        @param self
        @return
        '''
        self.insert_6lowpan_module()
        status, output = self.target.run('echo 1 > /sys/kernel/debug/bluetooth/6lowpan_enable')
        assert status == 0, "Enable ble 6lowpan fail: %s" % output
        # check file number, it should be 1
        status, output = self.target.run('cat /sys/kernel/debug/bluetooth/6lowpan_enable')
        if output == "1":
            pass
        else:
            target_collect_info('lsmod')
            assert False, "BLE 6lowpan interface is: %s\n%s" % (output, self.log) 

##
# @}
# @}
##

