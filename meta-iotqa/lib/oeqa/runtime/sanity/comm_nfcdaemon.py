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
        (status, output) = self.target.run('ps | grep neard -c')
        number = string.atoi(output)
        ##
        # TESTPOINT: #1, test_comm_nfcdaemoncheck
        #
        self.assertEqual(number, 3, msg="Error messages: %s" % output)

##
# @}
# @}
##

