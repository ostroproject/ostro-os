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
        """Parse result, transfer min to second
        @fn _parse_result
        @param self
        @param  data
        @return
        """
        boottime = 0.0
        if data:
		    min_result = re.search(r'(\d+)(min)', data)
		    if min_result:
			    boottime = boottime + int(min_result.group(1)) * 60.0
		    second_result = re.search(r'(\d+\.*\d*)(s)', data)
		    if second_result:
			    boottime = boottime + float(second_result.group(1))
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
        (status, output) = self.target.run("/tmp/systemd-analyze time"
                                           " | awk -F '=' '{print $2}'")
        result = self._parse_result(output)
        boottime = str(result)+"s"
        collect_pnp_log(casename, casename, boottime)
        print "\n%s:%s\n" % (casename, boottime)
        (status, output) = self.target.run("/tmp/systemd-analyze time")
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

