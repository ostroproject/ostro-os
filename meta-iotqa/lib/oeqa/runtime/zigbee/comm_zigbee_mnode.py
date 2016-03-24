"""
@file comm_zigbee_mnode.py
"""

##
# @addtogroup zigbee
# @brief This is component
# @{
# @addtogroup comm_zigbee
# @brief This is comm_zigbee module
# @{
##

import time
import os
import string
import zigbee
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import shell_cmd_timeout
from oeqa.utils.helper import run_as
from oeqa.utils.decorators import tag

@tag(TestType="FVT")
class ZigBeeMNode(oeRuntimeTest):
    """
    @class ZigBeeMNode
    """
    def setUp(self):
        ''' initialize zigbee class 
        @fn setUp
        @param self
        @return
        '''
        self.zigbee = zigbee.ZigBeeFunction(self.targets)

    @tag(FeatureID="IOTOS-1220")
    def test_zigbee_atmel_ping6(self):
        '''Setup two devices with atmel, and ping each other
        @fn test_zigbee_atmel_ping6
        @param self
        @return
        '''
        self.zigbee.atmel_enable_lowpan0(0)
        self.zigbee.atmel_enable_lowpan0(1)
        self.zigbee.lowpan0_ping6_check(0, 1)     

##
# @}
# @}
##

