#!/usr/bin/env python
#
# Author: Alexandru Cornea <alexandru.cornea@intel.com>

import unittest
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.decorators import *


@tag(TestType = 'FVT', FeatureID = 'IOTOS-539')
class TestAppDataProtection(oeRuntimeTest):
    """
    Testing app data protection
    Depends on pre-existent app to be installed

        application      | corresponding user created

        example-app-c    | yoyodine-nativetest
        example-app-node | iodine-nodetest
    """

    def test_native_app(self):
        path = "/apps/yoyodine/nativetest"
        target = "usr/bin/hello-world"

        status, output = self.target.run("ls -l %s/manifest" %path)
        if status != 0:
            raise unittest.SkipTest("example-app-c manifest not found")

        others_permissions = output.split()[0][7:10]
        self.assertNotIn("r", others_permissions,
                        "Read permission for others found for manifest")

        status, output = self.target.run("ls -l %s/%s" %(path, target))
        if status != 0:
            raise unittest.SkipTest("example-app-c executable not found")

        others_permissions = output.split()[0][7:10]
        self.assertNotIn("r", others_permissions,
                        "Read permission for others found for executable")

        self.assertNotIn("x", others_permissions,
                        "Execute permission for others found for executable")

    def test_node_app(self):
        path = "/apps/iodine/nodetest"
        target1 = "lib/node_modules/nodetest/example.js"
        target2 = "lib/node_modules/nodetest/package.json"

        status, output = self.target.run("ls -l %s/manifest" %path)
        if status != 0:
            raise unittest.SkipTest("example-app-node manifest not found")

        others_permissions = output.split()[0][7:10]
        self.assertNotIn("r", others_permissions,
                        "Read permission for others found for manifest")

        status, output = self.target.run("ls -l %s/%s" %(path, target1))
        if status != 0:
            raise unittest.SkipTest("example-app-node script not found")

        others_permissions = output.split()[0][7:10]
        self.assertNotIn("r", others_permissions,
                        "Read permission for others found for script")

        status, output = self.target.run("ls -l %s/%s" %(path, target2))
        if status != 0:
            raise unittest.SkipTest("example-app-node package.json not found")

        others_permissions = output.split()[0][7:10]
        self.assertNotIn("r", others_permissions,
                        "Read permission for others found for package.json")
