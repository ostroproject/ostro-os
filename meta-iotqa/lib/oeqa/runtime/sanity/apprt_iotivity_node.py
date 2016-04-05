"""
@file apprt_iotivity_node.py
"""

##
# @addtogroup sanity sanity
# @brief This is sanity component
# @{
# @addtogroup apprt_iotivity_node apprt_iotivity_node
# @brief This is apprt_iotivity_node module
# @{
##

import os
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.decorators import tag

@tag(TestType='EFT', FeatureID='IOTOS-764')
class SanityTestIotivityNode(oeRuntimeTest):
    """
    @class SanityTestIotivityNode
    """
    apprt_test_iotivity_node = 'apprt_test_iotivity_node.js'
    apprt_test_iotivity_node_target = '/tmp/%s' % apprt_test_iotivity_node

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
                SanityTestIotivityNode.apprt_test_iotivity_node),
            SanityTestIotivityNode.apprt_test_iotivity_node_target)


    def test_require_iotivity_node(self):
        '''
        Test if the node executable is installed and in PATH.
        @fn test_node_exists
        @param self
        @return
        '''
        (status, _) = self.target.run(
            'export NODE_PATH="/usr/lib/node_modules/"; \
            /usr/bin/node /tmp/apprt_test_iotivity_node.js')
        ##
        # TESTPOINT: #1, test_require_iotivity_node
        #
        self.assertEqual(
            status,
            0,
            msg='iotivity-node not in PATH or on target.')

    def tearDown(self):
        '''
        Clean work: remove all the files copied to the target device.
        @fn tearDown
        @param self
        @return
        '''
        self.target.run(
            'rm -f %s' %
            SanityTestIotivityNode.apprt_test_iotivity_node_target)

##
# @}
# @}
##

