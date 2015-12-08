import string
from oeqa.oetest import oeRuntimeTest

class CommDaemonTest(oeRuntimeTest):
    log = ""
    def target_collect_info(self, cmd):
        (status, output) = self.target.run(cmd)
        self.log = self.log + "\n\n[Debug] Command output --- %s: \n" % cmd
        self.log = self.log + output

    '''Connmand daemon check'''
    def test_comm_daemoncheck(self):
        '''check connman daemon'''
        (status, output) = self.target.run('systemctl status connman')
        if 'Active: active' in output:
            pass
        else:
            # Collect system information as log
            status=1
            self.target_collect_info("ps")
            self.target_collect_info("systemctl status connman -l")

        self.assertEqual(status, 0, msg="Error messages: %s" % self.log)
