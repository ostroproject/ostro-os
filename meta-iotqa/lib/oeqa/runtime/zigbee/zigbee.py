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

class ZigBeeFunction(object):
    """
    @class ZigBeeFunction
    """
    platform = ""
    atmel_mod_name = ""
    cc2520_mod_name = ""
    log = ""
    def __init__(self, target):
        self.target = target
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

##
# @}
# @}
##

