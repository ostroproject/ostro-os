"""
@file galileo_gen2.py
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

class GalileoGen2Test(oeRuntimeTest):
    """ BSP testing 
    @class GalileoGen2Test
    """

    def setUp(self):
        ''' setup the module name
        @fn setUp
        @param self
        @return
        '''
        self.spi_module_name = 'spi-quark-board'

    def tearDown(self):
        ''' remove spi module
        @fn tearDown
        @param self
        @return
        '''
        remove_module_cmd = "modprobe -r " + self.spi_module_name
        self.target.run(remove_module_cmd)

    @tag(FeatureID="IOTOS-1220")
    def test_galileo_gen2_spi(self):
        """ check Ostro on Galileo gen2 spi enablement
        @fn test_galiloe_gen2_spi
        @param self
        @return
        """

        insert_module_cmd = "modprobe " + self.spi_module_name

        (status,output) = self.target.run(insert_module_cmd)
        ##
        # TESTPOINT: check if the spi kernel module can be insert successfully
        #
        self.assertEqual(status, 0, msg="Error message: %s" % output)
        (status,output) = self.target.run("dmesg | tail")
        self.assertTrue((output.find("802.15.4 chip registered") >= 0), msg="Error message: the SPI module insert FAIL: %s" % output)

##
# @}
# @}
##

