#[PROTEXCAT]
#\License: ALL RIGHTS RESERVED
#\Author: Wang, Jing <jing.j.wang@intel.com>

'''base os test module'''
from oeqa.oetest import oeRuntimeTest

class BaseOsTest(oeRuntimeTest):
    '''Base os health check'''
    def test_baseos_dmesg(self):
        '''check dmesg command'''
        (status, output) = self.target.run('dmesg')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

    def test_baseos_lsmod(self):
        '''check lsmod command'''
        (status, output) = self.target.run('lsmod')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

    def test_baseos_ps(self):
        '''check ps command'''
        (status, output) = self.target.run('ps')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

    def test_baseos_df(self):
        '''check df command'''
        (status, output) = self.target.run('df')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

    def test_baseos_systemd_process(self):
        '''check systemd process'''
        (status, output) = self.target.run("ls -l /proc/1/exe | grep 'systemd'")
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

    def test_baseos_sensord_process(self):
        '''check sensord process'''
        (status, output) = self.target.run("ps | grep -v grep | grep sensord")
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
