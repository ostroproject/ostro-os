"""
@file appFW.py
"""

##
# @addtogroup misc misc
# @brief This is misc component
# @{
# @addtogroup appFW appFW
# @brief This is appFW module
# @{
##

from oeqa.oetest import oeRuntimeTest

class AppFwTest(oeRuntimeTest):
    """ App Framework testing 
    @class AppFwTest
    """


    def test_sqlite_integration(self):
        """ test sqlite is integrated in image 
        @fn test_sqlite_integration
        @param self
        @return
        """


        (status,output) = self.target.run("rpm -qa | grep sqlite")
        ##
        # TESTPOINT: #1, test_sqlite_integration
        #
        self.assertEqual(status, 0, output)

##
# @}
# @}
##

