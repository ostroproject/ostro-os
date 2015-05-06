from oeqa.oetest import oeRuntimeTest

class CommDaemonTest(oeRuntimeTest):
    '''Connmand daemon check'''
    def test_comm_daemoncheck(self):
        '''check connman daemon'''
        (status, output) = self.target.run('ps | grep connmand')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
