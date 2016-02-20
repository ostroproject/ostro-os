'''Reboot test module
@file reboot.py
'''

##
# @addtogroup sanity sanity
# @brief This is sanity component
# @{
# @addtogroup reboot reboot
# @brief This is reboot module
# @{
##

import time
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import shell_cmd_timeout

class RebootTest(oeRuntimeTest):
    '''Reboot target device
    @class RebootTest
    '''
    def setUp(self):
        '''pre condition check
        @fn setUp
        @param self
        @return
        '''
        self.assertTrue(self._alive(), msg="device is not alive before test")
   
    def _alive(self):
        '''check if device alive
        @fn _alive
        @param self
        @return
        '''
        #ret = shell_cmd_timeout("ssh -o ConnectTimeout=5 -o UserKnownHostsFile=/dev/null \
        #                             -o StrictHostKeyChecking=no root@%s '/bin/true'" % self.target.ip)[0]
        (ret, output) = self.target.run('/bin/true', 10)
        return True if ret == 0 else False

    def _wait_offline(self):
        '''wait till device offline
        @fn _wait_offline
        @param self
        @return
        '''
        for _ in range(60):
            if not self._alive():
                return True
            time.sleep(1)
        return False

    def _wait_online(self):
        '''wait till device online
        @fn _wait_online
        @param self
        @return
        '''
        for _ in range(60):
            if self._alive():
                return True
            time.sleep(1)
        return False

    def test_reboot(self):
        '''reboot target device
        @fn test_reboot
        @param self
        @return
        '''
        for cnt in range(1):
            print "Reboot %d time" % cnt
            ret = self.target.run('reboot &', 5)[0]
#            self.assertEqual(ret, 0, msg="Fail to trigger reboot command")
            time.sleep(4)
            status = self._wait_offline()
            ##
            # TESTPOINT: #1, test_reboot
            #
            self.assertTrue(status, msg="Fail to drive system off")
            time.sleep(4)
            status = self._wait_online()
            ##
            # TESTPOINT: #2, test_reboot
            #
            self.assertTrue(status, msg="Fail to bring up system")

##
# @}
# @}
##

