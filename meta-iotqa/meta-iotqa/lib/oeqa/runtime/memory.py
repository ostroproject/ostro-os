#[PROTEXCAT]
#\License: ALL RIGHTS RESERVED

'''Memory consumption for system idle'''
import time
from oeqa.oetest import oeRuntimeTest

class MemTest(oeRuntimeTest):
    
    def _reboot(self):
        ''' reboot device for clean env '''
        (status, output) = self.target.run("reboot")
        time.sleep(60)
        self.assertEqual(status, 0, output)

    def _setup(self):
        (status,output) = self.target.run("sleep 300 && sync && echo 1 >/proc/sys/vm/drop_cache")
        self.assertEqual(status, 0, output)

    def test_mem(self):
        self._reboot()
        self._setup()
        (status,output) = self.target.run("free | grep 'Mem' | awk '{print $3}'")
        self.assertEqual(status, 0, output)
