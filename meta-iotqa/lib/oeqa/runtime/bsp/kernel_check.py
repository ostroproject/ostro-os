"""
@file kernel_check.py
"""

##
# @addtogroup bsp bsp
# @brief This is bsp component
# @{
# @addtogroup bsp bsp
# @brief This is bsp module
# @{
##

import unittest
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.decorators import tag

@tag(TestType="FVT")

class KernelCheckTest(oeRuntimeTest):
    """ kernel check testing 
    @class KernelChecktest
    """

    def setUp(self):
        ''' define the kernel version
        @fn setUp
        @param self
        @return
        '''
        self.kernel_min_version = "4.4"
        self.platform_list = [ "intel-quark", "intel-corei7-64" ]

    def tearDown(self):
        ''' 
        @fn tearDown
        @param self
        @return
        '''
        pass

    @tag(FeatureID="IOTOS-1428")
    def test_kernel_version(self):
        """ check kernel version > min version
        @fn test_kernel_version
        @param self
        @return
        """
        (status,output) = self.target.run("uname -a | awk '{print $2}'")
        if status == 0:
            if output in self.platform_list: 
                ##
                # TESTPOINT: check if the kernel version is >= min version
                #
                (status,output) = self.target.run("uname -r | awk -F - '{print $1}'")
                self.assertEqual(status, 0, msg="Error message: %s" % output)
                self.assertTrue((output >= self.kernel_min_version), msg="Error message: the version (%s) is older than %s" % (output, self.kernel_min_version))
            else: 
                raise unittest.SkipTest("The platform %s is not for checking kernel version" % output)
        else: 
            raise unittest.SkipTest("Cannot get test platform correctly")
                
##
# @}
# @}
##

