"""
@file comm_btcheck.py
"""

##
# @addtogroup sanity sanity
# @brief This is sanity component
# @{
# @addtogroup comm_btcheck comm_btcheck
# @brief This is comm_btcheck module
# @{
##

import time
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.decorators import tag

@tag(TestType="FVT", FeatureID="IOTOS-453")
class CommBluetoothTest(oeRuntimeTest):
    """
    @class CommBluetoothTest
    """
    log = ""
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

    '''Bluetooth device check'''
    def test_comm_btcheck(self):
        '''check bluetooth device
        @fn test_comm_btcheck
        @param self
        @return
        '''
        # un-block software rfkill lock
        self.target.run('rfkill unblock all')
        # This is special for edison platform
        self.target.run('connmanctl enable bluetooth')
        time.sleep(8)
        # Collect system information as log
        self.target_collect_info("ifconfig")
        self.target_collect_info("hciconfig")
        self.target_collect_info("lsmod")
        # Detect BT device status
        (status, output) = self.target.run('hciconfig hci0')
        ##
        # TESTPOINT: #1, test_comm_btcheck
        #
        self.assertEqual(status, 0, msg="Error messages: %s" % self.log)

##
# @}
# @}
##

