"""
@file comm_ssh.py
"""

##
# @addtogroup sanity sanity
# @brief This is sanity component
# @{
# @addtogroup comm_ssh comm_ssh
# @brief This is comm_ssh module
# @{
##

import subprocess
import time
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.decorators import tag

@tag(TestType="FVT", FeatureID="IOTOS-489")
class CommSshTest(oeRuntimeTest):
    '''Ssh to logon target device
    @class CommSshTest
    '''
    def test_comm_ssh(self):
        '''check device ssh ability
        @fn test_comm_ssh
        @param self
        @return
        '''
        # Run any command by target.run method. if pass, it proves ssh is good
        (status, output) = self.target.run('uname -a')
        ##
        # TESTPOINT: #1, test_comm_ssh
        #
        self.assertEqual(status, 0, msg="Error messages: %s" % output)


##
# @}
# @}
##

