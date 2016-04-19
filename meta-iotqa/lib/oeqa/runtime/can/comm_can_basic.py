"""
@file comm_can_basic.py
"""

##
# @addtogroup can
# @brief This is component
# @{
# @addtogroup comm_can
# @brief This is comm_can
# @{
##

import can
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.decorators import tag

@tag(TestType="FVT")
class CommCAN(oeRuntimeTest):
    """
    @class CommCAN
    """
    def setUp(self):
        ''' initialize can class 
        @fn setUp
        @param self
        @return
        '''
        self.can = can.CANFunction(self.target)

    def tearDown(self):
        ''' disable after testing 
        @fn tearDown
        @param self
        @return
        '''
        # disable wifi
        self.can.disable_can()

    @tag(FeatureID="IOTOS-385")
    def test_enable_can0(self):
        '''Enable can0 interface on device
        @fn test_enable_can0
        @param self
        @return
        '''
        self.can.enable_can()

    @tag(FeatureID="IOTOS-385")
    def test_can_send_data(self):
        '''Send data to can bus
        @fn test_can_send_data
        @param self
        @return
        '''
        self.can.enable_can()
        self.can.send_data()

##
# @}
# @}
##

