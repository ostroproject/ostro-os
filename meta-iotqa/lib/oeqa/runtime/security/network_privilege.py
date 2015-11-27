#!/usr/bin/env python
#
# Author: Alexandru Cornea <alexandru.cornea@intel.com>
import unittest
import os
from time import sleep
from oeqa.oetest import oeRuntimeTest, skipModule
from oeqa.utils.decorators import *
from oeqa.utils.helper import get_files_dir

@tag(TestType = 'Functional Positive', FeatureID = 'IOTOS-807')
class NetworkPrivilege(oeRuntimeTest):
    """
    Testing local network and internet privilege enforcement
    Dependent on app-runas and smack
    """

    def setUp(self):
        self.user = "network-priv-user"
        idcmd="id -u %s" %self.user
        status, output = self.target.run(idcmd)
        if status:
                status, output = self.target.run("adduser -D %s" %self.user)
                self.assertFalse(status, msg="Adding %s user failed: %s" %(self.user, output))
                status, output = self.target.run(idcmd)
        self.assertTrue(output.isdigit(), msg="Unexpected output from %s: %s" %(idcmd, output))
        self.uid = output
        self.pkgid = "test-app-privilege"
        self.label = "test_label"
        status, output = self.target.run( "ls /tmp/app-runas")
        if status != 0:
                self.target.copy_to(
                        os.path.join(get_files_dir(), "app-runas"),
                        "/tmp/app-runas")

        status, output = self.target.run("mount | grep smackfs ")
        if status != 0:
            skipModule("Smack is not mounted")
        self.smack_path = output.split(" ")[2]

    def _alive(self):
        status, output = self.target.run("ping -c 1 %s" %self.target.ip)
        return not(bool(status))

    def _wait_smacknet(self):
        status = 1
        while status != 0:
            status, output = self.target.run("cat %s/netlabel | grep Network::Local" %self.smack_path)
            sleep(10)

    def test_app_no_network_privilege(self):
        """ Check if application without network privilege can access the network"""

        appid = "test-app-no-network-privilege"
        # install app
        self.target.run("/tmp/app-runas -a %s -p %s -u %s -i" % \
                        (appid, self.pkgid, self.uid))

        # check smack rule
        status, output = self.target.run("cat %s/load2 | grep 'User::App::%s Network::Local w'" \
                                            %(self.smack_path, appid))
        self.assertNotEqual(status, 0, "Smack rule for app without network privilege to have " + \
                                        "write access to network should not be set")

        status, output = self.target.run("cat %s/load2 | grep 'Network::Local User::App::%s w'" \
                                            %(self.smack_path, appid))
        self.assertNotEqual(status, 0, "Smack rule for network to have write access to app " + \
                                        "without privilege should not be set")

        self._wait_smacknet()
        # check ping
        status, output = self.target.run("/tmp/app-runas -a %s -u %s -e -- sh -c 'ping -c 3 %s'" \
                                            %(appid, self.uid, self.target.server_ip))

        self.assertIn("sendto: Permission denied", output, \
            "Application without network privilege can access to network")

    def test_app_with_network_privilege(self):
        """ Check if application with network privilege can access the network"""

        appid = "test-app-with-network-privilege"
        # install app
        self.target.run("/tmp/app-runas -a %s -p %s -u %s -r LocalNetworkAccess -i" \
                                    %(appid, self.pkgid, self.uid))

        # check smack rule
        status, output = self.target.run("cat %s/load2 | grep 'User::App::%s Network::Local w'" \
                                            %(self.smack_path, appid))
        self.assertEqual(status, 0, "Smack rule for app with local network privilege to have " + \
                                    "write access to network should be set %s" %output )

        status, output = self.target.run("cat %s/load2 | grep 'Network::Local User::App::%s w'" \
                                            %(self.smack_path, appid))
        self.assertEqual(status, 0, "Smack rule for network to have write access to app with " + \
                                    "local network privilege should be set. %s" %output)

        self._wait_smacknet()
        # check ping
        status, output = self.target.run("/tmp/app-runas -a %s -u %s -e -- sh -c 'ping -c 3 %s'" \
                                        %(appid, self.uid, self.target.server_ip))
        self.assertIn("3 packets transmitted, 3 packets received, 0% packet loss", \
                        output, "Application with network privilege cannot access network %s" %self.target.server_ip)

    def test_network_privilege_persistent_rules(self):
        """ Check app smack rules are persistent, remain after reboot """

        appid = "test-persistent-rules"

        # install app
        self.target.run("/tmp/app-runas -a %s -p %s -u %s -r LocalNetworkAccess -i" \
                            %(appid, self.pkgid, self.uid))

        # check smack rule
        status, output = self.target.run("cat %s/load2 | grep 'User::App::%s Network::Local w'" \
                                            %(self.smack_path, appid))
        self.assertEqual(status, 0, "Smack rule for app with local network privilege to have " + \
                                    "write access to network should be set")

        status, output = self.target.run("cat %s/load2 | grep 'Network::Local User::App::%s w'" \
                                            %(self.smack_path, appid))
        self.assertEqual(status, 0, "Smack rule for network to have write access to app with " + \
                                    "local network privilege should be set")

        # reboot
        self.target.run("reboot &")
        # give it time to shutdown
        sleep(10)
        no_tries = 10

        # wait for target to be alive
        while no_tries > 0 and not(self._alive()):
            sleep(20)
            no_tries -= 1

        if not self._alive():
           self.fail("Target did not come up after reboot")

        # check smack rule after reboot
        status, output = self.target.run("cat %s/load2 | grep 'User::App::%s Network::Local w'" \
                                            %(self.smack_path, appid))
        self.assertEqual(status, 0, "Smack rule for app to have write access to network " + \
                                    "was removed after reboot " )

        status, output = self.target.run("cat %s/load2 | grep 'Network::Local User::App::%s w'" \
                                            %(self.smack_path, appid))
        self.assertEqual(status, 0, "Smack rule for network to have write access to app " + \
                                    "was removed after reboot")

    def test_network_privilege_remove_app(self):
        appid = "test-remove-app"

        # install app
        self.target.run("/tmp/app-runas -a %s -p %s -u %s -r LocalNetworkAccess -i" % \
                            (appid, self.pkgid, self.uid))

        # check smack rule
        status, output = self.target.run("cat %s/load2 | grep 'User::App::%s Network::Local w'" \
                                            %(self.smack_path, appid))
        self.assertEqual(status, 0, "Smack rule for app with local network privilege to have " + \
                                    "write access to network should be set")

        status, output = self.target.run("cat %s/load2 | grep 'Network::Local User::App::%s w'" \
                                            %(self.smack_path, appid))
        self.assertEqual(status, 0, "Smack rule for network to have write access to app with " + \
                                    "local network privilege should be set")

        # remove app
        self.target.run("/tmp/app-runas -a %s -p %s -u %s -d" % \
                            (appid, self.pkgid, self.uid))

        # check smack rule
        status, output = self.target.run("cat %s/load2 | grep 'User::App::%s Network::Local w'" \
                                            %(self.smack_path, appid))
        self.assertNotEqual(status, 0, "Smack rule for app with local network privilege to have " + \
                                    "write access to network kept after app removal")

        status, output = self.target.run("cat %s/load2 | grep 'Network::Local User::App::%s w'" \
                                            %(self.smack_path, appid))
        self.assertNotEqual(status, 0, "Smack rule for network to have write access to app with " + \
                                    "local network privilege kept after app removal")

    def test_app_no_internet_privilege(self):
        """ Check if application without internet privilege can access the cloud"""

        appid = "test-app-no-internet-privilege"
        # install app
        self.target.run("/tmp/app-runas -a %s -p %s -u %s -i" % \
                        (appid, self.pkgid, self.uid))

        # check smack rule
        status, output = self.target.run("cat %s/load2 | grep 'User::App::%s Network::Cloud w'" \
                                            %(self.smack_path, appid))
        self.assertNotEqual(status, 0, "Smack rule for app without internet privilege to have " + \
                                        "write access to cloud should not be set")

        status, output = self.target.run("cat %s/load2 | grep 'Network::Cloud User::App::%s w'" \
                                            %(self.smack_path, appid))
        self.assertNotEqual(status, 0, "Smack rule for cloud to have write access to app " + \
                                        "without privilege should not be set")

        self._wait_smacknet()
        # check Internet Access
        # ping might not always work, proxies may be in the way
        # it is better to have some backup
        status, output1 = self.target.run("/tmp/app-runas -a %s -u %s -e -- sh -c 'ping -c 3 www.intel.com'" \
                                            %(appid, self.uid))
        status1 = int(" 0% packet loss" not in output)

        status, output2 = self.target.run("/tmp/app-runas -a %s -u %s -e -- sh -c 'ping -c 3 8.8.8.8'" \
                                            %(appid, self.uid))
        status2 = int(" 0% packet loss" not in output)

        status, output3 = self.target.run("/tmp/app-runas -a %s -u %s -e -- sh -c 'wget -T 3 -P /tmp/ www.intel.com'" \
                                            %(appid, self.uid))
        # if wget succeeded, index.html file will be created.
        # removing it will return 0 if the file exists
        status3, output = self.target.run("rm /tmp/index.html")

        status, output4 = self.target.run("/tmp/app-runas -a %s -u %s -e -- sh -c 'wget -T 3 -P /tmp/ www.google.com'" \
                                            %(appid, self.uid))
        # if wget succeeded, index.html file will be created.
        # removing it will return 0 if the file exists
        status4, output = self.target.run("rm /tmp/index.html")

        # if any of the above succeded, then status is True
        status = status1 and status2 and status3 and status4
        output = output1 + output2 + output3 + output4
        self.assertNotEqual(status, 0, "Application without internet privilege can access it. Output: %s" %output)

    def test_app_with_internet_privilege(self):
        """ Check if application with internet privilege can access the cloud"""


        appid = "test-app-with-internet-privilege"
        # install app
        self.target.run("/tmp/app-runas -a %s -p %s -u %s -r InternetAccess -i" \
                                    %(appid, self.pkgid, self.uid))

        # check smack rule
        status, output = self.target.run("cat %s/load2 | grep 'User::App::%s Network::Cloud w'" \
                                            %(self.smack_path, appid))
        self.assertEqual(status, 0, "Smack rule for app with internet privilege to have " + \
                                    "write access to cloud should be set %s" %output )

        status, output = self.target.run("cat %s/load2 | grep 'Network::Cloud User::App::%s w'" \
                                            %(self.smack_path, appid))
        self.assertEqual(status, 0, "Smack rule for cloud to have write access to app with " + \
                                    "internet privilege should be set. %s" %output)

        self._wait_smacknet()
        # check Internet Access
        # ping might not always work, proxies may be in the way
        # it is better to have some backup
        status, output1 = self.target.run("/tmp/app-runas -a %s -u %s -e -- sh -c 'ping -c 3 www.intel.com'" \
                                            %(appid, self.uid))
        status1 = int(" 0% packet loss" not in output1)

        status, output2 = self.target.run("/tmp/app-runas -a %s -u %s -e -- sh -c 'ping -c 3 8.8.8.8'" \
                                            %(appid, self.uid))
        status2 = int(" 0% packet loss" not in output2)

        status, output3 = self.target.run("/tmp/app-runas -a %s -u %s -e -- sh -c 'wget -T 3 -P /tmp/ www.intel.com'" \
                                            %(appid, self.uid))
        # if wget succeeded, index.html file will be created.
        # removing it will return 0 if the file exists
        status3, output = self.target.run("rm /tmp/index.html")

        status, output4 = self.target.run("/tmp/app-runas -a %s -u %s -e -- sh -c 'wget -T 3 -P /tmp/ www.google.com'" \
                                            %(appid, self.uid))
        # if wget succeeded, index.html file will be created.
        # removing it will return 0 if the file exists
        status4, output = self.target.run("rm /tmp/index.html")

        # if any of the above attempts passed, then status should be True
        status = status1 and status2 and status3 and status4
        output = output1 + output2 + output3 + output4
        self.assertEqual(status, 0, "Application with internet privilege cannot access it. Output: %s" %output)

    def test_internet_privilege_persistent_rules(self):
        """ Check app smack rules are persistent, remain after reboot """

        appid = "test-persistent-rules"

        # install app
        self.target.run("/tmp/app-runas -a %s -p %s -u %s -r InternetAccess -i" \
                            %(appid, self.pkgid, self.uid))

        # check smack rule
        status, output = self.target.run("cat %s/load2 | grep 'User::App::%s Network::Cloud w'" \
                                            %(self.smack_path, appid))
        self.assertEqual(status, 0, "Smack rule for app with internet privilege to have " + \
                                    "write access to cloud should be set")

        status, output = self.target.run("cat %s/load2 | grep 'Network::Cloud User::App::%s w'" \
                                            %(self.smack_path, appid))
        self.assertEqual(status, 0, "Smack rule for cloud to have write access to app with " + \
                                    "internet privilege should be set")

        # reboot
        self.target.run("reboot &")
        # give it time to shutdown
        sleep(10)
        no_tries = 10

        # wait for target to be alive
        while no_tries > 0 and not(self._alive()):
            sleep(20)
            no_tries -= 1

        if not self._alive():
           self.fail("Target did not come up after reboot")

        # check smack rule after reboot
        status, output = self.target.run("cat %s/load2 | grep 'User::App::%s Network::Cloud w'" \
                                            %(self.smack_path, appid))
        self.assertEqual(status, 0, "Smack rule for app to have write access to cloud " + \
                                    "was removed after reboot " )

        status, output = self.target.run("cat %s/load2 | grep 'Network::Cloud User::App::%s w'" \
                                            %(self.smack_path, appid))
        self.assertEqual(status, 0, "Smack rule for cloud to have write access to app " + \
                                    "was removed after reboot")

    def test_internet_privilege_remove_app(self):
        appid = "test-internet-remove-app"

        # install app
        self.target.run("/tmp/app-runas -a %s -p %s -u %s -r InternetAccess -i" % \
                            (appid, self.pkgid, self.uid))

        # check smack rule
        status, output = self.target.run("cat %s/load2 | grep 'User::App::%s Network::Cloud w'" \
                                            %(self.smack_path, appid))
        self.assertEqual(status, 0, "Smack rule for app with internet privilege to have " + \
                                    "write access to cloud should be set")

        status, output = self.target.run("cat %s/load2 | grep 'Network::Cloud User::App::%s w'" \
                                            %(self.smack_path, appid))
        self.assertEqual(status, 0, "Smack rule for cloud to have write access to app with " + \
                                    "internet privilege should be set")

        # remove app
        self.target.run("/tmp/app-runas -a %s -p %s -u %s -d" % \
                            (appid, self.pkgid, self.uid))

        # check smack rule
        status, output = self.target.run("cat %s/load2 | grep 'User::App::%s Network::Cloud w'" \
                                            %(self.smack_path, appid))
        self.assertNotEqual(status, 0, "Smack rule for app with internet privilege to have " + \
                                    "write access to cloud kept after app removal")

        status, output = self.target.run("cat %s/load2 | grep 'Network::Cloud User::App::%s w'" \
                                            %(self.smack_path, appid))
        self.assertNotEqual(status, 0, "Smack rule for cloud to have write access to app with " + \
                                    "internet privilege kept after app removal")
