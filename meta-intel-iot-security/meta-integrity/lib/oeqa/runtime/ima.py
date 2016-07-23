#!/usr/bin/env python
#
# Authors:  Cristina Moraru <cristina.moraru@intel.com>
#           Alexandru Cornea <alexandru.cornea@intel.com>

import unittest
import string
from time import sleep
from oeqa.oetest import oeRuntimeTest, skipModule
from oeqa.utils.decorators import *

@tag(TestType = 'FVT', FeatureID = 'IOTOS-617,IOTOS-619')
class IMACheck(oeRuntimeTest):
    def test_ima_before_systemd(self):
        ''' Test if IMA policy is loaded before systemd starts'''

        ima_search = "IMA: policy update completed"
        systemd_search = "systemd .* running"
        status, output = self.target.run("dmesg | grep -n '%s'" %ima_search)
        self.assertEqual( status, 0, "Did not find '%s' in dmesg" %ima_search)
        ima_id = int(output.split(":")[0])
        status, output = self.target.run("dmesg | grep -n '%s'" %systemd_search)
        self.assertEqual(status, 0, "Did not find '%s' in dmesg" %systemd_search)
        init_id = int(output.split(":")[0])
        if ima_id > init_id:
            self.fail("IMA does not start before systemd")

    def test_ima_hash(self):
        ''' Test if IMA stores correct file hash '''
        filename = "/etc/filetest"
        ima_measure_file = "/sys/kernel/security/ima/ascii_runtime_measurements"
        status, output = self.target.run("echo test > %s" %filename)
        self.assertEqual(status, 0, "Cannot create file %s on target" %filename)

        # wait for the IMA system to update the entry
        maximum_tries = 30
        tries = 0
        status, output = self.target.run("sha1sum %s" %filename)
        current_hash = output.split()[0]
        ima_hash = ""

        while tries < maximum_tries:
            status, output = self.target.run("cat %s | grep %s" \
                                            %(ima_measure_file, filename))
            # get last entry, 4th field
            if status == 0:
                tokens = output.split("\n")[-1].split()[3]
                ima_hash = tokens.split(":")[1]
                if ima_hash == current_hash:
                    break

            tries += 1
            sleep(1)

        # clean target
        self.target.run("rm %s" %filename)
        if ima_hash != current_hash:
            self.fail("Hash stored by IMA does not match actual hash")

    def test_ima_signature(self):
        ''' Test if IMA stores correct signature for system binaries'''
        locations = ["/bin", "/usr/bin"]
        binaries = []
        for l in locations:
            status, output = self.target.run("find %s -type f" %l)
            binaries.extend(output.split("\n"))

        for b in binaries:
            status, output = self.target.run("evmctl ima_verify %s" %b)
            if "Verification is OK" not in output:
                self.fail("IMA signature verification fails for file %s" %b)

    def test_ima_overwrite(self):
        ''' Test if IMA prevents overwriting signed files '''
        signed_file = "/bin/sh"
        status, output = self.target.run(" echo 'foo' >> %s" %signed_file)
        self.assertIn("Text file busy", output,
                      "Did not find expected error message. Got: %s" %output)
