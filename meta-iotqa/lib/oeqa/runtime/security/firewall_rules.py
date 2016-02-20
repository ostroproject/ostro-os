#!/usr/bin/env python
#
# Author: Alexandru Cornea <alexandru.cornea@intel.com>

import unittest
import os
import subprocess
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.decorators import *
from oeqa.utils.helper import get_files_dir


@tag(TestType = 'FVT', FeatureID = 'IOTOS-1229')
class TestFirewallRules(oeRuntimeTest):
    """
    Testing default firewall rules
    """

    def test_ipv4_incoming_packet(self):
        p = subprocess.Popen("ping -c 3 %s" %self.target.ip,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            shell=True )

        output, error = p.communicate()
        self.assertNotEqual(p.returncode, 0,
                            "Incoming packets should be dropped")

    def test_ipv4_outgoing_packet(self):
        status, output = self.target.run("ping -c 3 %s" %self.target.server_ip)

        self.assertEqual(status, 0,
                            "Outgoing packets should be sent succesfully")

    def test_ipv6_incoming_icmp(self):
        cmd = "ip addr show | grep inet6 | grep -v '::1/128'"
        status, output = self.target.run(cmd)

        ipv6 = output.split('\n')[0].split()[1].split("/")[0]
        p = subprocess.Popen("ping6 -c 3 %s" %ipv6,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            shell=True )

        output, error = p.communicate()
        self.assertNotEqual(p.returncode, 0,
                            "Incoming ipv6 icmp packets should be received")

    def test_ipv6_outgoing_icmp(self):
        cmd = "ip addr show | grep inet6 | grep -v '::1/128'"
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, shell=True)

        output, error = p.communicate()
        # get first ipv6 address
        ipv6 = output.split("\n")[0].split()[1].split("/")[0]
        status1 = 1
        if ipv6:
            status1, output = self.target.run("ping6 -c 3 %s" %ipv6)

        status2, output = self.target.run("ping6 -c 3 ipv6.google.com")

        # we need either one to succeed, in case the host
        # does not support ipv6
        self.assertEqual(status1 * status2, 0,
                        "Outgoing ipv6 packets should be sent")
