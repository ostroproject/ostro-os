"""
@file apprt_nodejs.py
"""

##
# @addtogroup sanity sanity
# @brief This is sanity component
# @{
# @addtogroup apprt_nodejs apprt_nodejs
# @brief This is apprt_nodejs module
# @{
##

import os
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.decorators import tag

@tag(TestType='FVT', FeatureID='IOTOS-332,IOTOS-1068')
class SanityTestNodejs(oeRuntimeTest):
    """
    @class SanityTestNodejs
    """

    apprt_test_node_helloworld = 'apprt_test_nodejs_helloworld.js'
    apprt_test_node_helloworld_target = '/tmp/%s' % apprt_test_node_helloworld

    def setUp(self):
        '''
        Copy all necessary files for test to the target device.
        @fn setUp
        @param self
        @return
        '''
        self.target.copy_to(
            os.path.join(
                os.path.dirname(__file__),
                'files',
                SanityTestNodejs.apprt_test_node_helloworld),
            SanityTestNodejs.apprt_test_node_helloworld_target)


    def test_node_exists(self):
        '''
        Test if the node executable is installed and in PATH.
        @fn test_node_exists
        @param self
        @return
        '''
        (status, _) = self.target.run('which node')
        ##
        # TESTPOINT: #1, test_node_exists
        #
        self.assertEqual(
            status,
            0,
            msg='node binary not in PATH or on target.')


    def test_node_version(self):
        '''
        Test if the version of node executable is OK.
        The expected version of node must be greater than or equal to v4.2.4
        @fn test_node_version
        @param self
        @return
        '''
        (status, output) = self.target.run('node -v')
        ##
        # TESTPOINT: #1, test_node_version
        #
        self.assertEqual(
            status,
            0,
            msg='v option for node command is invalid or node does not work.')
        target_version = output.strip().lstrip('v')
        if target_version.endswith('-pre'):
            target_version = target_version.rstrip('-pre')
        (major, minor, patch) = target_version.split('.')
        ##
        # TESTPOINT: #2, test_node_version
        #
        self.assertTrue(
            major.isdigit() and minor.isdigit() and patch.isdigit(),
            msg='The node version number is invalid!')
        version_num = int(major) * 10000 + int(minor) * 100 + int(patch)
        ##
        # TESTPOINT: #3, test_node_version
        #
        self.assertTrue(
            version_num >= 40204,
            msg='node version must not be less than 4.2.4!')


    def test_node_helloworld(self):
        '''
        Test if the simple hello world test program of node works well.        
        @fn test_node_helloworld
        @param self
        @return
        '''
        (status, output) = self.target.run('node %s' %
                           SanityTestNodejs.apprt_test_node_helloworld_target)
        ##
        # TESTPOINT: #1, test_node_helloworld
        #
        self.assertEqual(
            status,
            0,
            msg='Exit status was not 0. Output: %s' %
            output)
        ##
        # TESTPOINT: #2, test_node_helloworld
        #
        self.assertEqual(
            output,
            'Hello World!',
            msg='Incorrect output: %s' %
            output)


    def tearDown(self):
        '''
        Clean work: remove all the files copied to the target device.
        @fn tearDown
        @param self
        @return
        '''
        self.target.run(
            'rm -f %s' %
            SanityTestNodejs.apprt_test_node_helloworld_target)

##
# @}
# @}
##

