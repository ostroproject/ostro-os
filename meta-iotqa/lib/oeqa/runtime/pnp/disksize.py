#[PROTEXCAT]
#\License: ALL RIGHTS RESERVED

"""
@file disksize.py
"""

##
# @addtogroup pnp pnp
# @brief This is pnp component
# @{
# @addtogroup disksize disksize
# @brief This is disksize module
# @{
##

import os
import time
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import collect_pnp_log

class DiskSizeTest(oeRuntimeTest):
    """Disk consumption
    @class DiskSizeTest
    """

    
    def test_disksize(self):
        """use df command to calculate the image installed size
        @fn test_disksize
        @param self
        @return
        """
        filename = os.path.basename(__file__)
        casename = os.path.splitext(filename)[0]
        (status, output) = self.target.run(
            "df | grep '/dev' | "
            "awk '{sum+=$3} END {print sum/1024}'")
        collect_pnp_log(casename, casename, output)
        print "\n%s:%s\n" % (casename, output)
        ##
        # TESTPOINT: #1, test_disksize
        #
        self.assertEqual(status, 0, output)

        (status, output) = self.target.run("df -h")
        logname = casename + "-detail"
        collect_pnp_log(casename, logname, output)
        


##
# @}
# @}
##

