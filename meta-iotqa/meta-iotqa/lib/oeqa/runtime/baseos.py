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
