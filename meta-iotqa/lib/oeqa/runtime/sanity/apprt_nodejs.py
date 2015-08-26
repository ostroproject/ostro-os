import os
from oeqa.oetest import oeRuntimeTest


class SanityTestNodejs(oeRuntimeTest):

    apprt_test_node_helloworld = 'apprt_test_nodejs_helloworld.js'
    apprt_test_node_helloworld_target = '/tmp/%s' % apprt_test_node_helloworld

    def setUp(self):
        self.target.copy_to(
            os.path.join(
                os.path.dirname(__file__),
                'files',
                SanityTestNodejs.apprt_test_node_helloworld),
            SanityTestNodejs.apprt_test_node_helloworld_target)

    def test_node_exists(self):
        (status, _) = self.target.run('which node')
        self.assertEqual(
            status,
            0,
            msg='node binary not in PATH or on target.')

    def test_node_version(self):
        (status, output) = self.target.run('node -v')
        self.assertEqual(
            status,
            0,
            msg='v option for node command is invalid or node does not work.')
        target_version = output.strip().lstrip('v')
        if target_version.endswith('-pre'):
            target_version = target_version.rstrip('-pre')
        (major, minor, patch) = target_version.split('.')
        self.assertTrue(
            major.isdigit() and minor.isdigit() and patch.isdigit(),
            msg='The node version number is invalid!')
        version_num = int(major) * 10000 + int(minor) * 100 + int(patch)
        self.assertTrue(
            version_num >= 1207,
            msg='node version must not be less than 0.12.7!')


    def test_node_helloworld(self):
        (status, output) = self.target.run('node %s' %
                           SanityTestNodejs.apprt_test_node_helloworld_target)
        self.assertEqual(
            status,
            0,
            msg='Exit status was not 0. Output: %s' %
            output)
        self.assertEqual(
            output,
            'Hello World!',
            msg='Incorrect output: %s' %
            output)

    def tearDown(self):
        self.target.run(
            'rm -f %s' %
            SanityTestNodejs.apprt_test_node_helloworld_target)
