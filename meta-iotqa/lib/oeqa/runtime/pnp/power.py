#[PROTEXCAT]
#\License: ALL RIGHTS RESERVED

"""
@file power.py
"""

##
# @addtogroup pnp pnp
# @brief This is pnp component
# @{
# @addtogroup power power
# @brief This is power module
# @{
##

import os
import time
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import collect_pnp_log, shell_cmd_timeout

class PowerTest(oeRuntimeTest):
    """Use Daxin power monitor to measure system idle power
    @class PowerTest
    """


    def _setup(self):
        """The test requires power control program:rs2
        @fn _setup
        @param self
        @return
        """
        (status, output) = self.target.run("reboot &")
        time.sleep(100)
        ret = shell_cmd_timeout("ping -c 1 %s" %self.target.ip, 4)[0]
        if ret != 0:
            return False
        else:
            time.sleep(10)

    def test_power(self):
        """Measure power consumption
        @fn test_power
        @param self
        @return
        """
        self._setup()
        filename = os.path.basename(__file__)
        casename = os.path.splitext(filename)[0]
        
        powermonitor="/dev/ttyUSB0"
        resistance=0
        voltage=12
        measure_time=120

        (status, output) = shell_cmd_timeout("timeout %d rs2 %s %d %d > /tmp/power.log" 
                % (measure_time, powermonitor, resistance, voltage))
        (status, output) = shell_cmd_timeout("cat /tmp/power.log | "
                "awk '{sum+=$4} END {print sum/NR}'")
        ##
        # TESTPOINT: #1, test_power
        #
        self.assertEqual(status, 0, output)
        collect_pnp_log(casename, casename, output)
        print "\n%s:%s\n" % (casename, output)

        (status, output) = shell_cmd_timeout(
            "cat /tmp/power.log")
        logname = casename + "-detail"
        collect_pnp_log(casename, logname, output) 

##
# @}
# @}
##

