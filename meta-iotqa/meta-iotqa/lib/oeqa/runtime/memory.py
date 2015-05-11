#[PROTEXCAT]
#\License: ALL RIGHTS RESERVED

"""Memory consumption for system idle"""
import os
import time
from oeqa.oetest import oeRuntimeTest
from oeqa.runtime.helper import collect_pnp_log

class MemTest(oeRuntimeTest):
    
    def _reboot(self):
        """reboot device for clean env"""
        (status, output) = self.target.run("reboot")
        time.sleep(120)
        self.assertEqual(status, 0, output)

    def _setup(self):
        """First set sleep time to 180s (default 300s)"""
        (status,output) = self.target.run("sleep 180 && sync && echo 1 >/proc/sys/vm/drop_caches")
        self.assertEqual(status, 0, output)

    def test_mem(self):
        #self._reboot()
        self._setup()
        filename=os.path.basename(__file__)
        casename=os.path.splitext(filename)[0]
        (status,output) = self.target.run("free | grep 'Mem' | awk '{print $3}'")
        collect_pnp_log(casename, output)        
        print "\n%s:%s\n" %(casename, output)
        self.assertEqual(status, 0, output)
  
