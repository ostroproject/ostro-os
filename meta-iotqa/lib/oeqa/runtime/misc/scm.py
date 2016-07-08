"""
@file scm.py
"""

##
# @addtogroup misc misc
# @brief This is misc component
# @{
# @addtogroup scm scm
# @brief This is scm module
# @{
##

from oeqa.oetest import oeRuntimeTest
from oeqa.utils.decorators import tag

@tag(TestType="FVT", FeatureID="IOTOS-722")

class ScmTest(oeRuntimeTest):
    """ Misc/scm testing 
    @class ScmTest
    """


    def test_multiple_partition_image(self):
        """ check Ostro image has multiple partition  
        @fn test_multiple_partition_image
        @param self
        @return
        """


        (status,output) = self.target.run("cat /proc/partitions | grep -v major | grep -v ^$ | grep -v ram |wc -l")
        ##
        # TESTPOINT: check there are more than 1 partitions
        #
        self.assertEqual(status, 0, msg="Error message: %s" % output)
        self.assertTrue((int(output) > 1), msg="Error message: the partition is %s" % output)

##
# @}
# @}
##

