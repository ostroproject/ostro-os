#[PROTEXCAT]
#\License: ALL RIGHTS RESERVED

import os
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import collect_pnp_log, shell_cmd, get_files_dir

class NetperfTest(oeRuntimeTest):

    """Use netperf to measure the network speed"""

    def _setup(self):
        """Please make sure your network Env is Gigabit network"""
        (status, output) = self.target.copy_to(
            os.path.join(get_files_dir(),'netperf'),
            "/tmp/netperf")
        self.assertEqual(
            status,
            0,
            msg="netperf could not be copied. Output: %s" %
            output)
        (status, output) = self.target.run(" ls -la /tmp/netperf")
        self.assertEqual(
            status,
            0,
            msg="Failed to find netperf command")
        #ret = shell_cmd("/usr/bin/netserver")

    def test_netperf(self):
        self._setup()
        filename = os.path.basename(__file__)
        casename = os.path.splitext(filename)[0]
        
        (status, output) = self.target.run(
            "/tmp/netperf -t TCP_STREAM -l 60 -H %s"
            ">/tmp/netperf-detail.log" % self.target.server_ip)
        
        (status, output) = self.target.run(
            "cat /tmp/netperf-detail.log | tail -1 | awk '{print $5}'")
        netperf_res = output + "Mb/s"
        collect_pnp_log(casename, casename, netperf_res)
        print "\n%s:%s\n" % (casename, netperf_res)
        self.assertEqual(status, 0, netperf_res)

        (status, output) = self.target.run(
            "cat /tmp/netperf-detail.log")
        logname = casename + "-detail"
        collect_pnp_log(casename, logname, output)
