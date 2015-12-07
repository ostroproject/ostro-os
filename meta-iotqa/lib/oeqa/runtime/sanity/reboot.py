'''Reboot test module'''
import time
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import shell_cmd_timeout

class RebootTest(oeRuntimeTest):
    '''Reboot target device'''
    def setUp(self):
        '''pre condition check'''
        self.assertTrue(self._alive(), msg="device is not alive before test")
   
    def _alive(self):
        '''check if device alive'''
        ret = shell_cmd_timeout("ping -c 1 %s" % self.target.ip, 4)[0]
        return True if ret == 0 else False

    def _wait_offline(self):
        '''wait till device offline'''
        for _ in range(60):
            if not self._alive():
                return True
            time.sleep(1)
        return False

    def _wait_online(self):
        '''wait till device online'''
        for _ in range(60):
            if self._alive():
                return True
        return False

    def test_reboot(self):
        '''reboot target device'''
        for cnt in range(1):
            print "Reboot %d time" % cnt
            ret = self.target.run('reboot &')[0]
#            self.assertEqual(ret, 0, msg="Fail to trigger reboot command")
            time.sleep(4)
            status = self._wait_offline()
            self.assertTrue(status, msg="Fail to drive system off")
            time.sleep(4)
            status = self._wait_online()
            self.assertTrue(status, msg="Fail to bring up system")
