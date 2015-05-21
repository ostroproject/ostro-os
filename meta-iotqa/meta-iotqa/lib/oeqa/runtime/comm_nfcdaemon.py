import string
from oeqa.oetest import oeRuntimeTest

class CommNFCDaemonTest(oeRuntimeTest):
    '''Neard daemon check'''
    def test_comm_nfcdaemoncheck(self):
        '''check neard daemon'''
        (status, output) = self.target.run('ps | grep neard -c')
        number = string.atoi(output)
        self.assertEqual(number, 3, msg="Error messages: %s" % output)
