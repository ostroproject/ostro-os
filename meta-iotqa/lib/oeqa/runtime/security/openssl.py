#!/usr/bin/env python
#
# Author: Alexandru Cornea <alexandru.cornea@intel.com>

import unittest
import os
import random
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.decorators import *
from oeqa.utils.helper import get_files_dir


@tag(TestType = 'FVT', FeatureID = 'IOTOS-424')
class TestOpenSSL(oeRuntimeTest):
    """
    Testing openssl
    Requires ptest already installed
    """

    def test_openssl(self):
        cmd = "cd /usr/lib/openssl/ptest/ && ./run-ptest"
        status, output = self.target.run(cmd)
        self.assertEqual(status, 0, "OpenSSL ptest did not run succesfully")
        self.assertNotIn("FAIL:", output, "Some OpenSSL tests failed")
