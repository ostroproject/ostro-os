#[PROTEXCAT]
#\License: ALL RIGHTS RESERVED

"""
@file memory.py
"""

##
# @addtogroup pnp pnp
# @brief This is pnp component
# @{
# @addtogroup memory memory
# @brief This is memory module
# @{
##

import os
import time
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import collect_pnp_log


class MemTest(oeRuntimeTest):
    """Memory consumption for system idle
    @class MemTest
    """


    def _reboot(self):
        """reboot device for clean env
        @fn _reboot
        @param self
        @return
        """
        (status, output) = self.target.run("reboot")
        time.sleep(120)
        self.assertEqual(status, 0, output)

    def _setup(self):
        """First set sleep time to 180s (default 300s)
        @fn _setup
        @param self
        @return
        """
        (status, output) = self.target.run("sleep 180")
        self.assertEqual(status, 0, output)

    def test_mem(self):
        """Mem_Used = Mem_Total - Mem_Available
        @fn test_mem
        @param self
        @return
        """
        # self._reboot()
        self._setup()
        filename = os.path.basename(__file__)
        casename = os.path.splitext(filename)[0]
        (status, output) = self.target.run(
            "cat /proc/meminfo" " | grep 'MemTotal' | awk '{print $2}'")
        mem_total = int(output)
        (status, output) = self.target.run(
            "cat /proc/meminfo" " | grep 'MemAvailable' | awk '{print $2}'")
        mem_available = int(output)
        mem_used = str(mem_total - mem_available) + "KB"
        collect_pnp_log(casename, casename, mem_used)
        print "\n%s:%s\n" % (casename, mem_used)
        ##
        # TESTPOINT: #1, test_mem
        #
        self.assertEqual(status, 0, mem_used)

        (status, output) = self.target.run(
            "cat /proc/meminfo")
        logname = casename + "-meminfo"
        collect_pnp_log(casename, logname, output)

##
# @}
# @}
##

