"""
@file bsp.py
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

class BspTest(oeRuntimeTest):
    """ BSP testing 
    @class BsPTest
    """

    @tag(FeatureID="IOTOS-638")
    def test_bsp_version(self):
        """ check Ostro image bsp version 
        @fn test_bsp_version
        @param self
        @return
        """


        (status,output) = self.target.run("uname -r | awk -F - '{print $1}'")
        ##
        # TESTPOINT: check if the kernel version is > 4.1
        #
        self.assertEqual(status, 0, msg="Error message: %s" % output)
        self.assertTrue((output > '4.1'), msg="Error message: the version (%s) is older than 4.1" % output)

##
# @}
# @}
##

