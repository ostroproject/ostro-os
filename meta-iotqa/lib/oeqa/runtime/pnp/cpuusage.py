#[PROTEXCAT]
#\License: ALL RIGHTS RESERVED

"""
@file cpuusage.py
"""

##
# @addtogroup pnp pnp
# @brief This is pnp component
# @{
# @addtogroup cpuusage cpuusage
# @brief This is cpuusage module
# @{
##

import os
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import collect_pnp_log

class CPUUsageTest(oeRuntimeTest):
    """CPU consumption for system idle
    @class CPUUsageTest
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
    
    def test_cpuusage(self):
        """Measure system idle CPU usage
        @fn test_cpuusage
        @param self
        @return
        """
        # self._reboot()
        filename = os.path.basename(__file__)
        casename = os.path.splitext(filename)[0]
        (status, output) = self.target.run(
            "top -b -d 10 -n 12 >/tmp/top.log")
        (status, output) = self.target.run(
            "cat /tmp/top.log | grep -i 'CPU' | grep 'id*' | "
            "tail -10 | awk '{print $8}' | "
            "awk -F '%' '{sum+=$1} END {print sum/NR}'")
        cpu_idle = float(output)
        cpu_idle = float("{0:.2f}".format(cpu_idle))
        cpu_used = str(100 - cpu_idle) + "%"
        collect_pnp_log(casename, casename, cpu_used)
        print "\n%s:%s\n" % (casename, cpu_used)
        ##
        # TESTPOINT: #1, test_cpuusage
        #
        self.assertEqual(status, 0, cpu_used)

        (status, output) = self.target.run(
            "cat /tmp/top.log")
        logname = casename + "-topinfo"
        collect_pnp_log(casename, logname, output)

##
# @}
# @}
##

