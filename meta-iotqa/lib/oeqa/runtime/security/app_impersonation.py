#!/usr/bin/env python
#
# Author: Alexandru Cornea <alexandru.cornea@intel.com>

import unittest
import os
import random
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.decorators import *
from oeqa.utils.helper import get_files_dir


@tag(TestType = 'FVT', FeatureID = 'IOTOS-416,IOTOS-418')
class TestAppImpersonation(oeRuntimeTest):
    """
    Testing App impersonation prevention
    Depends on pre-existent app to be installed

        application      | corresponding user created

        example-app-c    | yoyodine-nativetest
        example-app-node | iodine-nodetest

    """
    def setUp(self):
        self.user1 = "yoyodine-nativetest"
        self.user2 = "iodine-nodetest"

    def _check_shadow_user(self,output):
        pass_hash = output.split(":")[1]
        return (pass_hash in ["*", "!"])

    def test_app_user_shadow(self):
        shadow = "/etc/shadow"
        skip = True

        status, output = self.target.run("grep '%s' %s"
                                            %(self.user1, shadow))
        if status == 0:
            # user exists
            result = self._check_shadow_user(output)
            self.assertEqual(result, True, "User %s has a password" %self.user1)
            skip = False

        status, output = self.target.run("grep %s %s"
                                            %(self.user2, shadow))
        if status == 0:
            # user exists
            result = self._check_shadow_user(output)
            self.assertEqual(result, True, "User %s has a password" %self.user2)
            skip = False

        if skip:
            raise unittest.SkipTest("Application users not found")

    def test_app_user_passwd(self):
        passwd = "/etc/passwd"
        login = "/sbin/nologin"
        skip = True
        status, output = self.target.run("grep %s %s" %(self.user1, passwd))
        if status == 0:
            # user exists
            self.assertIn(login, output, "User %s has a different login: %s"
                                %(self.user1, output.split(":")[-1]))
            skip = False

        status, output = self.target.run("grep %s %s" %(self.user2, passwd))
        if status == 0:
            # user exists
            self.assertIn(login, output, "User %s has a different login: %s"
                                %(self.user2, output.split(":")[-1]))

            skip = False

        if skip:
            raise unittest.SkipTest("Application users not found")

    def test_app_nonexistent_group(self):

        service_file = "/run/systemd/generator/evil-bad-groups.service"
        to_search = "SupplementaryGroups="
        group1 = "nonexistent1"
        group2 = "nonexistent2"

        status, output = self.target.run("ls %s" %service_file)

        if status != 0:
            raise unittest.SkipTest("Application bad-groups-app not found")

        status, output = self.target.run("grep %s %s" %(to_search,service_file))

        self.assertNotIn(group1, output,
                        "App was assigned to nonexistent group: %s" %group1)

        self.assertNotIn(group1, output,
                        "App was assigned to nonexistent group: %s" %group2)
