#!/usr/bin/env python
#
# Author: Alexandru Cornea <alexandru.cornea@intel.com>

import unittest
import os
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.decorators import *
from oeqa.utils.helper import get_files_dir


@tag(TestType = 'FVT', FeatureID = 'IOTOS-415')
class AppMemoryProtection(oeRuntimeTest):
    """
    Testing application memory protection.
    This includes shared memory segments and ptrace scope protection

    Depends on read-map, shm-util, gdb
    """

    def _add_user(self, user):
        """
        checks if user exists, and adds it if not
        """
        status, output = self.target.run("id -u %s" %user)
        if status != 0:
            self.target.run("useradd -M %s" %user)

    def test_read_map(self):
        """
        checks that a process cannot read memory that has not been mapped to it
        """
        status, output = self.target.run("ls /tmp/read-map")
        if status != 0:
            self.target.copy_to(
                    os.path.join(get_files_dir(), "read-map"),
                    "/tmp/read-map")

        status, output = self.target.run("/tmp/read-map")
        # expected to exit with segmentation fault (signal 11 - SEGV)
        # exit code: 128 + 11(SEGV)
        self.assertEqual(status, 139, "Process did not exit with segfault")


    def test_ptrace_scope_protection_child(self):
        """
        Checks ptrace scope to be set. Any result except 0 is considered success

        kernel.yama.ptrace_scope0: all processes can be debugged, as long as
        they have same uid. This is the classical way of how ptracing worked.
        kernel.yama.ptrace_scope = 1: only a parent process can be debugged.
        kernel.yama.ptrace_scope = 2: Only admin can use ptrace, as it required
        CAP_SYS_PTRACE capability.
        kernel.yama.ptrace_scope = 3: No processes may be traced with ptrace.
        Once set, a reboot is needed to enable ptracing again.
        """

        ptrace_file = "/proc/sys/kernel/yama/ptrace_scope"

        status, output = self.target.run("cat %s" %ptrace_file)
        self.assertEqual(status, 0, "Cannot read file %s" %ptrace_file)

        ptrace_scope = int(output)
        self.assertNotEqual(ptrace_scope, 0,
                            "Ptrace scope protection not enabled")


    def test_shmem_protection(self):
        """
        Uses shm-util as an alternative to ipcmk, ipcrm
        If ipcmk, ipcrm, ipcs becomes available, they could be used instead
        """
        status, output = self.target.run("ls /tmp/shm-util")
        if status != 0:
            self.target.copy_to(
                    os.path.join(get_files_dir(), "shm-util"),
                    "/tmp/shm-util")

        # need 2 users
        # right now we can add them
        # in the future, we might need 2 apps pre-installed
        user1 = "test-app1"
        user2 = "test-app2"
        self._add_user(user1)
        self._add_user(user2)

        shm_create_cmd = "/tmp/shm-util -m 2048 -p 0600"
        status, shm_id = self.target.run("su %s -c -- sh -c '%s'" \
                                            %(user1, shm_create_cmd))
        shm_id = shm_id.split(":")[1]
        self.assertEqual(status, 0, "Unable to create shared memory segment")

        shm_remove_cmd = "/tmp/shm-util -r %s" %shm_id
        status, output = self.target.run("su %s -c -- sh -c '%s'" \
                                            %(user2, shm_remove_cmd))

        self.assertNotEqual(
                        status, 0,
                        "Shared memory segment could be access by another user")

        # clean up
        self.target.run("su %s -c -- sh -c '/tmp/shm-util -r %s" \
                        %(user1, shm_id))

    def test_no_gdb(self):
        """
        checks that another user cannot use gdb to attach to an already running
        process of another user
        """
        # get pid of a process
        # chose systemd-timesyncd
        process = "systemd-timesyncd"
        status, pid = self.target.run("pidof %s" %process)
        self.assertEqual(status, 0, "Unable to get pid of %s" %process)

        # run as user nobody
        # might need to change this in the future
        user = "nobody"
        self._add_user(user)
        expected = "ptrace: Operation not permitted."
        status, output = self.target.run("su %s -c 'gdb -p %s --batch'" \
                                            %(user,pid))
        self.assertIn(expected, output,
                        "GDB trace of another user's processes should fail")
