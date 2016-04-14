#!/usr/bin/env python
#
# Author: Alexandru Cornea <alexandru.cornea@intel.com>

import unittest
import os
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.decorators import *
from oeqa.utils.helper import get_files_dir


@tag(TestType = 'FVT', FeatureID = 'IOTOS-1228')
class DacTestConfig(oeRuntimeTest):
    """
    Testing DAC configuration
    """


    def _add_user(self, user, group):
        """
        checks if user exists, and adds it if not
        """
        status, output = self.target.run("id -u %s" %user)
        if status != 0:
            self.target.run("useradd -M %s -g %s" %(user, group))

    def setUp(self):
        self.user1 = "dac1"
        self.user2 = "dac2"
        self.user3 = "dac3"

        self.groupA = "groupA"
        self.groupB = "groupB"
        status, output = self.target.run("addgroup %s" %self.groupA)
        status, output = self.target.run("addgroup %s" %self.groupB)
        self._add_user(self.user1, self.groupA)
        self._add_user(self.user2, self.groupA)
        self._add_user(self.user3, self.groupB)

        self.target.run("touch /tmp/file{1,2,3}")
        self.target.run("chown %s:%s /tmp/file{1,2,3}" %(self.user1, self.groupA))
        self.target.run("chmod 700 /tmp/file1")
        self.target.run("chmod 770 /tmp/file2")
        self.target.run("chmod 777 /tmp/file3")

        # if smack is enabled, make sure it does not block access
        # "Any access on label star(*) is permitted"
        status, output = self.target.run("mount | grep smackfs ")
        if status == 0:
            self.target.run("chsmack -a '*' /tmp/file{1,2,3}")

    def test_same_group_no_access(self):

        status, output = self.target.run("su %s -c -- 'echo test > /tmp/file1'"
                                        %self.user2)
        expected = "sh: /tmp/file1: Permission denied"
        self.assertIn(expected, output,
                            "Same group, no access, could write file ")

    def test_same_group_with_access(self):

        status, output = self.target.run("su %s -c -- 'echo test > /tmp/file2'"
                                        %self.user2)

        self.assertEqual(status, 0,
                            "Same group, with access, could not write file ")

    def test_others_no_access(self):
        status, output = self.target.run("su %s -c -- 'echo test > /tmp/file1'"
                                        %self.user3)

        self.assertNotEqual(status, 0,
                            "Others group, no access, could write file ")

        status, output = self.target.run("su %s -c -- 'echo test > /tmp/file2'"
                                        %self.user3)

        expected = "sh: /tmp/file2: Permission denied"
        self.assertIn(expected, output,
                            "Others group, no access, could write file ")

    def test_others_with_access(self):

        status, output = self.target.run("su %s -c -- 'echo test > /tmp/file3'"
                                        %self.user3)

        self.assertEqual(status, 0,
                            "Others group, with access, could not write file ")
