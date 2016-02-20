#[PROTEXCAT]
#\License: ALL RIGHTS RESERVED

"""
@file iozone.py
"""

##
# @addtogroup pnp pnp
# @brief This is pnp component
# @{
# @addtogroup iozone iozone
# @brief This is iozone module
# @{
##

import os
import time
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import collect_pnp_log, get_files_dir

class IOzoneTest(oeRuntimeTest):
    """Use IOzone to measure storage read/write speed
    @class IOzoneTest
    """


    def _setup(self):
        """
        @fn _setup
        @param self
        @return
        """
        (status, output) = self.target.copy_to(
            os.path.join(get_files_dir(),'iozone'), "/tmp/iozone")
        self.assertEqual(
            status,
            0,
            msg="iozone could not be copied. Output: %s" %
            output)
        (status, output) = self.target.run(" ls -la /tmp/iozone")
        self.assertEqual(
            status,
            0,
            msg="Failed to find iozone command")

    def test_iozone(self):
        """Use IOzone to measure storage read/write speed
        @fn test_iozone
        @param self
        @return
        """
        self._setup()
        filename = os.path.basename(__file__)
        casename = os.path.splitext(filename)[0]
        
        (status, output) = self.target.run(
            "/tmp/iozone -a -i 0 -i 1 -s 512M -r 1M"
            ">/tmp/iozone-detail.log")
        
        (status, output) = self.target.run(
            "cat /tmp/iozone-detail.log | tail -4 | "
            "grep '524288'| awk '{print $5/1024}'")
        read_res = "Read: " + output + "MB/s"
        
        (status, output) = self.target.run(
            "cat /tmp/iozone-detail.log | tail -4 | "
            "grep '524288'| awk '{print $3/1024}'")
        write_res = "Write:" + output + "MB/s"
        
        collect_pnp_log(casename, casename, read_res)
        collect_pnp_log(casename, casename, write_res)
        print "\n%s:%s %s\n" % (casename, read_res, write_res)
        ##
        # TESTPOINT: #1, test_iozone
        #
        self.assertEqual(status, 0, read_res)

        (status, output) = self.target.run(
            "cat /tmp/iozone-detail.log")
        logname = casename + "-detail"
        collect_pnp_log(casename, logname, output)

##
# @}
# @}
##

