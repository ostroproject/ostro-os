"""
@file soletta_dev_app.py
"""

##
# @addtogroup soletta
# @brief This is soletta component
# @{
# @addtogroup soletta_dev_app
# @brief This is soletta_dev_app module
# @{
##

import os
import time
import subprocess
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import shell_cmd_timeout
from oeqa.utils.helper import get_files_dir
from oeqa.utils.decorators import *

class SolettaDevAppTest(oeRuntimeTest):
    """
    @class SolettaDevAppTest
    """
    def setUp(self):
        ''' initialize soletta dev app test class 
        @fn setUp
        @param self
        @return
        '''
        self.sda_location = ''
        self.sda_pid = ''

    @tag(TestType="FVT")
    @tag(FeatureID="IOTOS-1468")
    def test_sda_server_integration(self):
        ''' check if the soletta-dev-app server start up after Ostro bootup
        @fn test_sda_server_integration
        @param self
        @return
        '''

        (status, output) = self.target.run('ps -ef | grep node | grep soletta-dev-app')
        self.assertEqual(status, 0, msg="Cannot find the soletta-dev-app server start: %s" % output)
        cmd_list = output.split()
        sda_app = [ s for s in cmd_list if 'app.js' in s ]
        self.assertFalse((not sda_app), msg="Cannot find app.js and soletta-dev-app server should not start")
        self.sda_location = os.path.dirname(os.path.abspath(sda_app[0]))
        self.assertFalse((not self.sda_location), msg="Cannot get soletta-dev-app location")
        self.sda_pid = cmd_list[1]
        self.assertFalse((not self.sda_pid), msg="Cannot get soletta-dev-app pid")

    @tag(TestType="FVT")
    @tag(FeatureID="IOTOS-1468")
    @skipUnlessPassed("test_server_integration")
    def test_sda_server_restart(self):
        ''' restart soletta-dev-app server with default configuration
        @fn test_sda_server_restart
        @param self
        @return
        '''
        (status, output) = self.target.run('systemctl stop soletta-dev-app-server.service')
        self.assertEqual(status, 0, msg="Error to stop soletta-dev-app server: %s" % output)
        # sleep 5 seconds to ensure the server stopped
        time.sleep(5)
        (status, output) = self.target.run('systemctl start soletta-dev-app-server.service')
        self.assertEqual(status, 0, msg="Error message: %s" % output)
        # sleep 5 seconds to ensure the server started
        time.sleep(5)
        
        (status, output) = self.target.run('ps -ef | grep node | grep soletta-dev-app')
        self.assertEqual(status, 0, msg="Cannot find the soletta-dev-app server restart: %s" % output)
        cmd_list = output.split()
        sda_app = [ s for s in cmd_list if 'app.js' in s ]
        sda_pid = cmd_list[1]
        self.assertNotEqual(sda_pid, self.sda_pid, msg="new start soledda-dev-app pid is same as initial one")
##
# @}
# @}
##

