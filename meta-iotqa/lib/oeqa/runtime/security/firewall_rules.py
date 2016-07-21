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
        expected= "3 packets transmitted, 0 received, 100% packet loss"
        self.assertIn(expected, output.decode('ascii'),
                            "Incoming packets should be dropped")

    def test_ipv4_outgoing_packet(self):
        status, output = self.target.run("ping -c 3 %s" %self.target.server_ip)

        expected = "3 packets transmitted, 3 packets received, 0% packet loss"
        self.assertIn(expected, output,
                            "Outgoing packets should be sent succesfully")

    def test_ipv6_incoming_icmp(self):
        cmd = "ip addr show | grep -A 2 %s | grep inet6 | awk '{print $2}'" %self.target.ip
        status, output = self.target.run(cmd)
        ipv6 = output.strip().split('/')[0]
        # get current interface
        cmd = "ip addr show | grep %s" %self.target.server_ip

        p = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            shell=True)

        output, error = p.communicate()
        interface = output.decode('ascii').strip().split()[-1]

        p = subprocess.Popen("ping6 -I %s -c 3 %s" %(interface, ipv6),
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            shell=True )

        output, error = p.communicate()
        expected = "3 packets transmitted, 3 received, 0% packet loss"
        self.assertIn(expected, output.decode('ascii'),
                            "Incoming ipv6 icmp packets should be received")

    def test_ipv6_outgoing_icmp(self):
        cmd = "ip addr show | grep -A 2 %s | grep inet6 | awk '{print $2}'" %self.target.server_ip
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, shell=True)

        output, error = p.communicate()
        # get ipv6 address
        ipv6 = output.decode('ascii').strip().split('/')[0]

        cmd = "ip addr show | grep %s" %self.target.ip
        status, output = self.target.run(cmd)
        interface = output.strip().split()[-1]
        status1, output = self.target.run("ping6 -I %s -c 3 %s"
                                                %(interface, ipv6))

        status2, output = self.target.run("ping6 -I %s -c 3 ipv6.google.com"
                                            %interface)

        # we need either one to succeed, in case the host
        # does not support ipv6
        self.assertEqual(status1 * status2, 0,
                        "Outgoing ipv6 packets should be sent")
