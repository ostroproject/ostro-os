#[PROTEXCAT]
#\License: ALL RIGHTS RESERVED

'''System boot time'''
from oeqa.oetest import oeRuntimeTest

class BootTimeTest(oeRuntimeTest):
    
    def _setup(self):
        (status,output) = self.target.copy_to("systemd-analyze","/tmp/systemd-analyze")
        self.assertEqual(status, 0, msg="systemd-analyze could not be copied. Output: %s" % output)
        (status,output) = self.target.run(" ls -la /tmp/systemd-analyze")
        self.assertEqual(status, 0, msg="Failed to find systemd-analyze command")

    def test_boot_time(self):
        self._setup()
        (status,output) = self.target.run("/tmp/systemd-analyze time | awk -F '=' '{print $2}'")
        self.assertEqual(status, 0, output)
