"""
@file comm_ethernet.py
"""

##
# @addtogroup ethernet ethernet
# @brief This is ethernet component
# @{
# @addtogroup comm_ethernet comm_ethernet
# @brief This is comm_ethernet module
# @{
##

import time
import os
import string
import ConfigParser
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import shell_cmd_timeout
from oeqa.utils.decorators import tag

eth_config = ConfigParser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), "files/config.ini")
eth_config.readfp(open(config_path))

@tag(TestType="EFT")
class CommEthernet(oeRuntimeTest):
    """
    @class CommEthernet
    """
    def get_ipv6(self):
        """
        @fn get_ipv6
        @param self
        @return
        """
        time.sleep(1)
        # Check ip address by ifconfig command
        interface = "nothing"
        (status, interface) = self.target.run("ifconfig | grep '^enp' | awk '{print $1}'")
        (status, output) = self.target.run("ifconfig %s | grep 'inet6 addr:' | awk '{print $3}'" % interface)
        return output.split('%')[0]

    @tag(FeatureID="IOTOS-489")
    def test_ethernet_ipv6_ping(self):
        '''Ping other device via ipv6 address of the ethernet
        @fn test_ethernet_ipv6_ping
        @param self
        @return
        '''
        # Get target ipv6 address
        ip6_address = self.get_ipv6()
        # ping6 needs host's ethernet interface by -I, 
        # because default gateway is only for ipv4
        host_eth = eth_config.get("Ethernet","interface")
        cmd = "ping6 -I %s %s -c 1" % (host_eth, ip6_address) 
        status, output = shell_cmd_timeout(cmd, timeout=60)
        ##
        # TESTPOINT: #1, test_ethernet_ipv6_ping
        #
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

    @tag(FeatureID="IOTOS-489")
    def test_ethernet_ipv6_ssh(self):
        '''SSH other device via ipv6 address of the ethernet
        @fn test_ethernet_ipv6_ssh
        @param self
        @return
        '''
        # Get target ipv6 address
        ip6_address = self.get_ipv6()
        # Same as ping6, ssh with ipv6 also need host's ethernet interface
        # ssh root@<ipv6 address>%<eth>
        host_eth = eth_config.get("Ethernet","interface")
        exp = os.path.join(os.path.dirname(__file__), "files/ipv6_ssh.exp")
        cmd = "expect %s %s %s %s" % (exp, ip6_address, "ostro", host_eth)
        status, output = shell_cmd_timeout(cmd, timeout=60)
        # In expect, it will input yes and password while login. And do 'ls /'
        # If see /home folder, it will return 2 as successful status.
        ##
        # TESTPOINT: #1, test_ethernet_ipv6_ssh
        #
        self.assertEqual(status, 2, msg="Error messages: %s" % output)

##
# @}
# @}
##

