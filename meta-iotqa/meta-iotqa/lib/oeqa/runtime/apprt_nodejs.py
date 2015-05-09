import unittest
import os
from oeqa.oetest import oeRuntimeTest, skipModule
from oeqa.utils.decorators import *


def read_version(file_path, executable):
    version = {}
    # A configuration file must exist in the ./files directory
    # It store the version info of node, npm
    # the format is like this
    # 
    # node: 0.10.35
    # npm: 2.7.4
    with open(file_path) as f:
        for line in f:
            if not ':' in line:
                continue

            (app, ver) = line.strip().split(':')
            app = app.strip().lower()
            ver = ver.strip()
            version[app] = ver

    return version.get(executable)


class SanityTestNodejs(oeRuntimeTest):
    
    local_ver_file = os.path.join(oeRuntimeTest.tc.filesdir, 'apprt_version.txt')
    apprt_test_node_helloworld = 'apprt_test_nodejs_helloworld.js'
    apprt_test_node_helloworld_target = '/tmp/%s' % apprt_test_node_helloworld
    
    @classmethod
    def setUpClass(cls):
        oeRuntimeTest.tc.target.copy_to(os.path.join(oeRuntimeTest.tc.filesdir, SanityTestNodejs.apprt_test_node_helloworld),
        												SanityTestNodejs.apprt_test_node_helloworld_target)

    
    def test_node_exists(self):
        (status, output) = self.target.run('which node')
        self.assertEqual(status, 0, msg = 'node binary not in PATH or on target.')


    def test_node_version(self):
        pre_node_version = read_version(SanityTestNodejs.local_ver_file, 'node')
        (status, output) = self.target.run('node -v')
        self.assertEqual(status, 0, msg = 'v option for node command is invalid or node does not work.')
        target_version = output.strip().lstrip('v')
        self.assertEqual(target_version, pre_node_version, msg = 'node version: %s is expected but %s is found on target.' % (pre_node_version, target_version))


    def test_npm_exists(self):
        (status, output) = self.target.run('which npm')
        self.assertEqual(status, 0, msg = 'npm package not in PATH or on target.')


    def test_npm_version(self):
        pre_npm_version = read_version(SanityTestNodejs.local_ver_file, 'npm')
        (status, output) = self.target.run('npm -v')
        self.assertEqual(status, 0, msg = 'v option for npm is invalid or npm does not work.')
        target_version = output.strip()
        self.assertEqual(target_version, pre_npm_version, msg = 'npm version: %s is expected but %s is found on target.' % (pre_npm_version, target_version))


    def test_node_helloworld(self):
        (status, output) = self.target.run('node %s' % SanityTestNodejs.apprt_test_node_helloworld_target)
        self.assertEqual(status, 0, msg = 'Exit status was not 0. Output: %s' % output)
        self.assertEqual(output, 'Hello World!', msg = 'Incorrect output: %s' % output)


    @classmethod
    def tearDownClass(cls):
        oeRuntimeTest.tc.target.run('rm -f %s' % SanityTestNodejs.apprt_test_node_helloworld_target)


