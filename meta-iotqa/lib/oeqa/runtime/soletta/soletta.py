"""
@file soletta.py
"""

##
# @addtogroup soletta
# @brief This is soletta component
# @{
# @addtogroup soletta
# @brief This is soletta module
# @{
##

import os
import time
import subprocess
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import shell_cmd_timeout
from oeqa.utils.helper import get_files_dir
from oeqa.utils.decorators import *

class SolettaTest(oeRuntimeTest):
    """
    @class SolettaTest
    """
    def setUp(self):
        ''' initialize soletta dev app test class 
        @fn setUp
        @param self
        @return
        '''
        pass

    @tag(TestType="FVT")
    @tag(FeatureID="IOTOS-1467")
    def test_soletta_integration(self):
        ''' check if the soletta libraries, modules and binaries integration
        @fn test_soletta_integration
        @param self
        @return
        '''

        (status, output) = self.target.run('ls /usr/lib/libsoletta.so')
        self.assertEqual(status, 0, msg="Cannot find the soletta library: %s" % output)
        (status, output) = self.target.run('find /usr/lib/soletta/modules/ -name *.so')
        self.assertEqual(status, 0, msg="Cannot find the soletta modules: %s" % output)
        (status, output) = self.target.run('which sol-fbp-runner')
        self.assertEqual(status, 0, msg="Cannot find the sol-fbp-runner: %s" % output)
        (status, output) = self.target.run('which sol-fbp-generator')
        self.assertEqual(status, 0, msg="Cannot find the sol-fbp-generator: %s" % output)

#    @tag(TestType="FVT")
#    @tag(FeatureID="IOTOS-1468")
#    @skipUnlessPassed("test_server_integration")
##
# @}
# @}
##

