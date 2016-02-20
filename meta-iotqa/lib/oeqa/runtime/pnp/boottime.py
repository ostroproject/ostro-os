#[PROTEXCAT]
#\License: ALL RIGHTS RESERVED

"""
@file boottime.py
"""

##
# @addtogroup pnp pnp
# @brief This is pnp component
# @{
# @addtogroup boottime boottime
# @brief This is boottime module
# @{
##

import os
import re
import time
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import collect_pnp_log, get_files_dir


class BootTimeTest(oeRuntimeTest):
    """System boot time measurement
    @class BootTimeTest
    """

    def _setup(self):
        """Copy systemd-analyze to target device
        @fn _setup
        @param self
        @return
        """
        (status, output) = self.target.copy_to(
            os.path.join(get_files_dir(),
                         'systemd-analyze'), "/tmp/systemd-analyze")
        self.assertEqual(
            status,
            0,
            msg="systemd-analyze could not be copied. Output: %s" %
            output)
        (status, output) = self.target.run(" ls -la /tmp/systemd-analyze")
        self.assertEqual(
            status,
            0,
            msg="Failed to find systemd-analyze command")

    def _parse_result(self, data):
        """Parse systemd-analyze result to calculate boot time
        boot time = kernel time + userspace time
        @fn _parse_result
        @param self
        @param  data
        @return
        """
        boottime = 0.0
        if 'kernel' in data:
            pattern=re.compile(r'(\d*\.?\d*)[s]\s\(kernel\)')
            k_time=pattern.findall(data)
            pattern=re.compile(r'(\d*\.?\d*)[s]\s\(userspace\)')
            u_time=pattern.findall(data)
            if k_time and u_time:
                boottime = float(k_time[0]) +float(u_time[0])
        return boottime

    def test_boot_time(self):
        """Measure boot time with systemd-analyze
        @fn test_boot_time
        @param self
        @return
        """
        self._setup()
        time.sleep(60)
        filename = os.path.basename(__file__)
        casename = os.path.splitext(filename)[0]
        (status, output) = self.target.run("/tmp/systemd-analyze time")
        result = self._parse_result(output)
        boottime = str(result)+"s"
        collect_pnp_log(casename, casename, boottime)
        print "\n%s:%s\n" % (casename, boottime)
        logname = casename + "-systemd-analyze"
        collect_pnp_log(casename, logname, output)
        ##
        # TESTPOINT: #1, test_boot_time
        #
        self.assertEqual(status, 0, output)

##
# @}
# @}
##

