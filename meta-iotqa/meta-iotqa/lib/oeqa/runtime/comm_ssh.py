import subprocess
import time
from oeqa.oetest import oeRuntimeTest

class CommSshTest(oeRuntimeTest):
    '''Ssh to logon target device'''
    def test_comm_ssh(self):
        '''check device ssh ability'''
        # Run any command by target.run method. if pass, it proves ssh is good
        (status, output) = self.target.run('uname -a')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

