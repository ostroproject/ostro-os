#[PROTEXCAT]
#\License: ALL RIGHTS RESERVED

import os
import time
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import collect_pnp_log


class MemTest(oeRuntimeTest):

    """Memory consumption for system idle"""

    def _reboot(self):
        """reboot device for clean env"""
        (status, output) = self.target.run("reboot")
        time.sleep(120)
        self.assertEqual(status, 0, output)

    def _setup(self):
        """First set sleep time to 180s (default 300s)"""
        (status, output) = self.target.run("sleep 180")
        self.assertEqual(status, 0, output)

    def test_mem(self):
        """Mem_Used = Mem_Total - Mem_Available"""
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
        collect_pnp_log(casename, mem_used)
        print "\n%s:%s\n" % (casename, mem_used)
        self.assertEqual(status, 0, mem_used)
