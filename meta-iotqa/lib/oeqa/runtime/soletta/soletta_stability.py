"""
@file soletta_stability.py
"""

##
# @addtogroup soletta
# @brief This is soletta component
# @{
# @addtogroup soletta_stability
# @brief This is soletta_stability module
# @{
##

import os
import time
import subprocess
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import shell_cmd_timeout
from oeqa.utils.helper import get_files_dir
from oeqa.utils.decorators import tag

@tag(TestType="EFT")
class SolettaStabilityTest(oeRuntimeTest):
    """
    @class SolettaStabilityTest
    """
    def setUp(self):
        ''' initialize soletta test class 
        @fn setUp
        @param self
        @return
        '''
        (status, output) = self.target.run('if [ ! -d /tmp/soletta-stability ]; then mkdir /tmp/soletta-stability; else rm -rf /tmp/soletta-stability/*; fi')
        if (status != 0):
            self.assertEqual(status, 0, msg="/tmp/soletta-stability error: %s" % output)
        else:
            fbp_path = os.path.join(os.path.dirname(__file__), "files/soletta-stability.fbp")
            self.target.copy_to(fbp_path, "/tmp/soletta-stability")
            self.target.run('echo "test data" > /tmp/soletta-stability/1')
            self.target.run('echo "test data" > /tmp/soletta-stability/2')
            self.target.run('echo "test data" > /tmp/soletta-stability/3')
            self.target.run('echo "test data" > /tmp/soletta-stability/4')
            self.target.run('echo "test data" > /tmp/soletta-stability/5')
        

    def test_soletta_multiple_nodes_concurrently(self):
        ''' test multiple soletta nodes run concurrently
        @fn test_soletta_multiple_nodes_concurrently
        @param self
        @return
        '''

        (status, output) = self.target.run('sol-fbp-runner -c /tmp/soletta-stability/soletta-stability.fbp')
        self.assertEqual(status, 0, msg="Syntax Check Error: %s" % output)
        
        (status, output) = self.target.run('sol-fbp-runner /tmp/soletta-stability/soletta-stability.fbp')
        self.assertEqual(status, 0, msg="Error message: %s" % output)
        
##
# @}
# @}
##

