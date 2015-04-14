import unittest
from oeqa.oetest import oeRuntimeTest, skipModule
from oeqa.utils.decorators import *

def setUpModule():
    if not oeRuntimeTest.hasFeature('smack'):
        skipModule("smack module skipped: target doesn't have smack in DISTRO_FEATURES")

class SmackBasicTest(oeRuntimeTest):

    @skipUnlessPassed('test_ssh')
    def test_smack_labels(self):
        '''Check for correct Smack labels.'''
        expected = '''
/tmp access="*"
/etc access="System::Shared" transmute="TRUE"
/etc/skel access="User::Home"
/var/log access="System::Log"
/var/tmp access="*"
'''
        (status, output) = self.target.run('chsmack -L ' + ' '.join([x.split()[0] for x in expected.split('\n') if x]))
        self.assertEqual(status, 0, msg="status and output: %s and %s" % (status,output))
        self.assertEqual(output.strip(), expected.strip())
