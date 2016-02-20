#!/usr/bin/env python
#
# Author: Alexandru Cornea <alexandru.cornea@intel.com>

import unittest
import os
import random
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.decorators import *
from oeqa.utils.helper import get_files_dir


@tag(TestType = 'FVT', FeatureID = 'IOTOS-431')
class TestCACertificate(oeRuntimeTest):
    """
    Testing certificate management
    """

    def test_update_certificate(self):
        certs_dir = "/etc/ssl/certs"
        status, output = self.target.run("ls %s" %certs_dir)
        cert = random.choice(output.split())

        self.target.run("rm /etc/ssl/certs/%s" %cert)
        self.target.run("update-ca-certificates")

        status, output = self.target.run("ls %s/%s" %(certs_dir, cert))
        self.assertEqual(status, 0, "Certificate was not restored")
