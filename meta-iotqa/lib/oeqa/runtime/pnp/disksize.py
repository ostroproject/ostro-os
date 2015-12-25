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
import re
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import collect_pnp_log

class DiskSizeTest(oeRuntimeTest):
    """Disk consumption
    @class DiskSizeTest
    """


    def _parse_result(self, casename, logname):
        """parse disk size info from log file
        @param self
        @param casename
        @param logname
        @return disksize
        """
        logpath = os.path.join(".", casename, logname)
        file = open(logpath, 'r')
        lines = file.readlines()
        max = len(lines)
        disksize = ""
        index = max -1
        while index > 0:
            #search the latest data from the end line
            if '/dev/disk' in lines[index]:
                pattern = re.compile(r'(\d*\.?\d*[GM])')
                size = pattern.findall(lines[index])
                if len(size) > 1:
                    disksize = size[1]
                    break
                else:
                    #The result may be at the next line
                    size = pattern.findall(lines[index+1])
                    if len(size) > 1:
                        disksize = size[1]
                        break
                    else:
                        print "Failed to find disk size!"
                        break
            index = index -1
        file.close()
        return disksize

    def test_disksize(self):
        """use df command to calculate the image installed size
        @fn test_disksize
        @param self
        @return
        """
        filename = os.path.basename(__file__)
        casename = os.path.splitext(filename)[0]
        (status, output) = self.target.run("df -h")
        logname = casename + "-detail"
        collect_pnp_log(casename, logname, output)
        disksize = self._parse_result(casename,logname)
        collect_pnp_log(casename, casename, disksize)
        ##
        # TESTPOINT: #1, test_disksize
        #
        print "\n%s:%s\n" % (casename, output)
        self.assertEqual(status, 0, output)


        


##
# @}
# @}
##

