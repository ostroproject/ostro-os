"""
@file comm_nfcdaemon.py
"""

##
# @addtogroup sanity sanity
# @brief This is sanity component
# @{
# @addtogroup comm_nfcdaemon comm_nfcdaemon
# @brief This is comm_nfcdaemon module
# @{
##

import string
from oeqa.oetest import oeRuntimeTest

class CommNFCDaemonTest(oeRuntimeTest):
    '''Neard daemon check
    @class CommNFCDaemonTest
    '''
    def test_comm_nfcdaemoncheck(self):
        '''check neard daemon
        @fn test_comm_nfcdaemoncheck
        @param self
        @return
        '''
        (status, output) = self.target.run('systemctl status neard')
        if 'Active: active' in output:
            pass
        else:
            # Collect system information as log
            status=1

        ##
        # TESTPOINT: #1, test_comm_nfcdaemoncheck
        #
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

##
# @}
# @}
##
