"""
@file can.py
"""

##
# @addtogroup sanity sanity
# @brief This is sanity component
# @{
# @addtogroup comm_can
# @brief This is comm_can
# @{
##

import time
import os
import string
from oeqa.utils.helper import shell_cmd_timeout

class CANFunction(object):
    """
    @class CANFunction
    """
    log = ""
    def __init__(self, target):
        self.target = target

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

    def enable_can(self):
        """
        @fn enable_can
        @param self
        @return
        """
        # Check if the can-usb is recognized at system boot up
        (status, output) = self.target.run('ifconfig -a')
        if 'can0' not in output:
            # try to use scland to create can0 (for some CAN232 and CANUSBdevices)
            (status, output) = self.target.run('slcand -o -c -f -F /dev/ttyUSB0 can0 > /dev/null 2&>1 &')
            assert status == 0, "Error messages: %s" % output 

        (status, output) = self.target.run('ifconfig can0 up')
        assert status == 0, "Error messages: %s" % output
        time.sleep(1)

    def disable_can(self):
        ''' disable can0 after testing 
        @fn disable_can
        @param self
        @return
        '''
        (status, output) = self.target.run('ifconfig can0 down')
        assert status == 0, "Error messages: %s" % output 
        (status, output) = self.target.run('killall slcand')
        # sleep some seconds to ensure disable is done
        time.sleep(1)

    def send_data(self):
        """
        @fn send_data
        @param self
        """
        # after 10 seconds, send data to can-bus
        self.target.run('candump can0 > /tmp/can-log 2>&1 &')
        time.sleep(1)
        (status, output) = self.target.run('cansend can0 500#1E.10.11.10')
        assert status == 0, "cansend command fails: %s" % output
        # Check can-dump output
        self.target.run('killall candump')
        (status, output) = self.target.run('cat /tmp/can-log')
        if 'can0  500' in output:
            pass
        else:
            assert False, "can-dump does not get data: %s %s" % (output, self.log)

##
# @}
# @}
##

