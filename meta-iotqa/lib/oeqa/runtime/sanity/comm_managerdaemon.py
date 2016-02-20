"""
@file comm_managerdaemon.py
"""

##
# @addtogroup sanity sanity
# @brief This is sanity component
# @{
# @addtogroup comm_managerdaemon comm_managerdaemon
# @brief This is comm_managerdaemon module
# @{
##

import string
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.decorators import tag

@tag(TestType="FVT", FeatureID="IOTOS-462")
class CommDaemonTest(oeRuntimeTest):
    """
    @class CommDaemonTest
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

    '''Connmand daemon check'''
    def test_comm_daemoncheck(self):
        '''check connman daemon
        @fn test_comm_daemoncheck
        @param self
        @return
        '''
        (status, output) = self.target.run('systemctl status connman')
        if 'Active: active' in output:
            pass
        else:
            # Collect system information as log
            status=1
            self.target_collect_info("ps")
            self.target_collect_info("systemctl status connman -l")

        ##
        # TESTPOINT: #1, test_comm_daemoncheck
        #
        self.assertEqual(status, 0, msg="Error messages: %s" % self.log)

##
# @}
# @}
##

