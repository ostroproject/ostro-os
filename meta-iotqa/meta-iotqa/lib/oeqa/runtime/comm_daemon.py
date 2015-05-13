import string
from oeqa.oetest import oeRuntimeTest

class CommDaemonTest(oeRuntimeTest):
    '''Connmand daemon check'''
    def test_comm_daemoncheck(self):
        '''check connman daemon'''
        (status, output) = self.target.run('ps | grep systemd -c')
        number = string.atoi(output)
        self.assertEqual(number, 3, msg="Error messages: %s" % output)
