#[PROTEXCAT]
#\License: ALL RIGHTS RESERVED
#\Author: Wang, Jing <jing.j.wang@intel.com>

'''ping device test module'''
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import shell_cmd_timeout

class PingDevTest(oeRuntimeTest):
    '''Ping target device'''
    def test_ping_dev(self):
        '''Check connectivity by ping command'''
        cmd = "ping -c 5 %s" % self.target.ip
        ret, output = shell_cmd_timeout(cmd, timeout=16)
        self.assertEqual(ret, 0, msg="Fail to ping target:\n%s" % output)
