"""
@file edison.py
"""

##
# @addtogroup bsp bsp
# @brief This is bsp component
# @{
# @addtogroup bsp bsp
# @brief This is bsp module
# @{
##

from oeqa.oetest import oeRuntimeTest
from oeqa.utils.decorators import tag

@tag(TestType="FVT")

class EdisonTest(oeRuntimeTest):
    """ BSP testing 
    @class EdisonTest
    """

    def setUp(self):
        ''' setup the module name
        @fn setUp
        @param self
        @return
        '''
        pass

    def tearDown(self):
        ''' remove spi module
        @fn tearDown
        @param self
        @return
        '''
        pass

    @tag(FeatureID="IOTOS-1463")
    def test_edison_kernel(self):
        """ check Ostro on edison kernel
        @fn test_edison_kernel
        @param self
        @return
        """

        (status,output) = self.target.run("uname -r | awk -F - '{print $1}'")
        ##
        # TESTPOINT: check if the kernel version is >= 3.10.98
        #
        self.assertEqual(status, 0, msg="Error message: %s" % output)
        self.assertTrue((output >= '3.10.98'), msg="Error message: the version (%s) is older than 3.10.98" % output)

##
# @}
# @}
##

