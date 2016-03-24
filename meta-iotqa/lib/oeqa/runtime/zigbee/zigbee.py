"""
@file zigbee.py
"""

##
# @addtogroup zigbee
# @brief This is zigbee component
# @{
# @addtogroup comm_zigbee
# @brief This is comm_zigbee module
# @{
##

import time
import os
import string
from oeqa.utils.helper import shell_cmd_timeout
from oeqa.utils.helper import run_as

class ZigBeeFunction(object):
    """
    @class ZigBeeFunction
    """
    platform = ""
    atmel_mod_name = ""
    cc2520_mod_name = ""
    log = ""
    def __init__(self, targets):
        self.targets = targets
        self.target = targets[0]
        self.init_platform()

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

    def init_platform(self):
        '''based on uname -a, check which platform and its module name'''
        """
        @fn 
        @param self
        @return
        """
        (status, output) = self.target.run('uname -a')
        if "intel-quark" in output:
            self.platform="Galileo"
            self.atmel_mod_name="spi-quark-board"
        elif "intel-corei7-64" in output:
            # Here assume case is not played on GB-BXBT, for uname arch are same
            self.platform="MinnowMax"
            self.atmel_mod_name="spi-minnow-board"
            self.cc2520_mod_name="spi-minnow-cc2520"
        else:
            assert False, "The platform does not support 6lowpan. check: %s" % output

    def insert_atmel_mode(self):
        ''' Insert atmel modules 
        @fn insert_atmel_mode
        @param self
        @return
        '''
        (status, output) = self.target.run('dmesg -c')
        (status, output) = self.target.run('modprobe %s' % self.atmel_mod_name)
        assert status == 0, "Error messages: %s" % output 
        # Check dmesg log, to see if the 802.15.4 is registered
        (status, output) = self.target.run('dmesg')
        if "802.15.4 chip registered" in output:
            pass
        else:
            assert False, "Not initialize 802.15.4 module. see dmesg log:\n%s" % output 

    def insert_cc2520_mode(self):
        ''' Insert cc2520 modules 
        @fn insert_cc2520_mode
        @param self
        @return
        '''
        (status, output) = self.target.run('modprobe %s' % self.cc2520_mod_name)
        assert status == 0, "Error messages: %s" % output 
        # Check dmesg log, to see if the 802.15.4 is registered
        (status, output) = self.target.run('lsmod')
        if self.cc2520_mod_name in output:
            pass
        else:
            assert False, "Not initialize cc2520 module. see lsmod:\n%s" % output

    def atmel_enable_lowpan0(self, target_number):
        ''' enable atmel chipset on target 
        @fn atmel_enable_lowpan0
        @param self
        @param target_number: 0 stands for main_target, 1 stands for second target
        @return
        '''
        # get device ip for debug
        my_ip=self.targets[target_number].ip
      
        # insert module
        cmd='modprobe %s' % self.atmel_mod_name
        (status, output) = run_as('root', cmd, target=self.targets[target_number])
        time.sleep(1)
        assert status == 0, "[%s] Insert atmel module fails: %s" % (my_ip, output)
        # set wpan0
        ip_set="ip link set wpan0 address a0:0:0:0:0:0:0:%d" % (target_number+1)
        (status, output) = run_as('root', ip_set, target=self.targets[target_number]) 
        time.sleep(1)
        # set channel as 5
        wpan_set="iz set wpan0 777 800%d 5" % (target_number+1)
        (status, output) = run_as('root', wpan_set, target=self.targets[target_number]) 
        time.sleep(1)
        # bring up wpan0
        (status, output) = run_as('root', 'ifconfig wpan0 up', target=self.targets[target_number]) 
        time.sleep(1)
        assert status == 0, "[%s] Bring up wpan0 fails: %s" % (my_ip, output)
        # add lowpan0 
        (status, output) = run_as('root', 'ip link add link wpan0 name lowpan0 type lowpan', target=self.targets[target_number]) 
        time.sleep(1)
        # bring up lowpan0
        (status, output) = run_as('root', 'ifconfig lowpan0 up', target=self.targets[target_number]) 
        time.sleep(1)
        assert status == 0, "[%s] Bring up lowpan0 fails: %s" % (my_ip, output)

    def get_lowpan0_ip(self, target_number):  
        ''' Get lowpan0 (ipv6) address 
        @fn get_lowpan0_ip
        @param self
        @param target_number: 0 stands for main_target, 1 stands for second target
        @return
        '''
        cmd="ifconfig lowpan0 | grep 'inet6 addr:'"
        (status, output) = run_as('root', cmd, target=self.targets[target_number])
        return output.split('%')[0].split()[2]    

    def lowpan0_ping6_check(self, main, second):
        ''' On main target, run ping6 to ping second's ipv6 address 
        @fn ping6_check
        @param self
        @param main: main target number
        @param second: second target number 
        @return
        '''
        cmd='ping6 -I lowpan0 -c 1 %s' % self.get_lowpan0_ip(second)
        (status, output) = run_as('root', cmd, target=self.targets[main])
        assert status == 0, "Ping second target lowpan0 ipv6 address fail: %s" % output

##
# @}
# @}
##

