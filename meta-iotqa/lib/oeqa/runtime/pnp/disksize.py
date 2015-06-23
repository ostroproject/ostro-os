#[PROTEXCAT]
#\License: ALL RIGHTS RESERVED

import os
import time
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import collect_pnp_log

class DiskSizeTest(oeRuntimeTest):

    """Disk consumption"""
    
    def test_disksize(self):
        """use df command to calculate the image installed size"""
        filename = os.path.basename(__file__)
        casename = os.path.splitext(filename)[0]
        (status, output) = self.target.run(
            "df | grep '/dev' | "
            "awk '{sum+=$3} END {print sum/1024}'")
        collect_pnp_log(casename, casename, output)
        print "\n%s:%s\n" % (casename, output)
        self.assertEqual(status, 0, output)

        (status, output) = self.target.run("df -h")
        logname = casename + "-detail"
        collect_pnp_log(casename, logname, output)
        

