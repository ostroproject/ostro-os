'''Reboot test module'''
import time
from oeqa.oetest import oeRuntimeTest
from oeqa.runtime.helper import shell_cmd_timeout

class RebootTest(oeRuntimeTest):
    '''Reboot target device'''
    def _alive(self):
        '''check if device alive'''
        ret = shell_cmd_timeout("ping -c 1 %s" % self.target.ip, 4)[0]
        return True if ret == 0 else False

    def _wait_offline(self):
        '''wait till device offline'''
        for _ in range(60):
            time.sleep(2)
            if not self._alive():
                return True
        return False

    def _wait_online(self):
        '''wait till device online'''
        for _ in range(60):
            time.sleep(2)
            if self._alive():
                return True
        return False

    def test_reboot(self):
        '''reboot target device for several times'''
        for _ in range(3):
            ret = self.target.run('reboot')[0]
            self.assertEqual(ret, 0, msg="Fail to trigger reboot command")
            time.sleep(4)
            status = self._wait_offline()
            self.assertTrue(status, msg="Fail to drive system off")
            time.sleep(4)
            status = self._wait_online()
            self.assertTrue(status, msg="Fail to bring up system")
