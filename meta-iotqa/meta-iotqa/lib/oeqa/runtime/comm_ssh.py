import subprocess
import time
from oeqa.oetest import oeRuntimeTest

class CommSshTest(oeRuntimeTest):
    '''Ssh to logon target device'''
    def test_comms_ssh(self):
        '''Check ssh logon'''
        output = ''
        proc = subprocess.Popen("ssh root@%s" % self.target.ip,
                                   shell=True, stdout=subprocess.PIPE)
        self.assertEqual(proc.poll(), 0, msg=\
                    "Expected ssh return 0, got command return %d.\
                     ping output is:\n%s" % (proc.poll(), output))
