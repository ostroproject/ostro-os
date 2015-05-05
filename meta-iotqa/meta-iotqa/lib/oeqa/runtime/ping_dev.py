import subprocess
import time
from oeqa.oetest import oeRuntimeTest

class PingDevTest(oeRuntimeTest):
    '''Ping target device'''
    def test_ping_dev(self):
        '''Check connectivity by ping command'''
        output = ''
        count = 0
        endtime = time.time() + 60
        while count < 5 and time.time() < endtime:
            proc = subprocess.Popen("ping -c 1 %s" % self.target.ip,
                                       shell=True, stdout=subprocess.PIPE)
            output += proc.communicate()[0]
            if proc.poll() == 0:
                count += 1
            else:
                count = 0
        self.assertEqual(count, 5, msg=\
                    "Expected 5 consecutive replies, got %d.\
                     ping output is:\n%s" % (count, output))
