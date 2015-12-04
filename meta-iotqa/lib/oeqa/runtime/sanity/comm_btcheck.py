from oeqa.oetest import oeRuntimeTest

class CommBluetoothTest(oeRuntimeTest):
    log = ""
    def target_collect_info(self, cmd):
        (status, output) = self.target.run(cmd)
        self.log = self.log + "\n\n[Debug] Command output --- %s: \n" % cmd
        self.log = self.log + output

    '''Bluetooth device check'''
    def test_comm_btcheck(self):
        '''check bluetooth device'''
        # un-block software rfkill lock
        self.target.run('rfkill unblock all')
        # This is special for edison platform
        self.target.run('connmanctl enable bluetooth')
        # Collect system information as log
        self.target_collect_info("ifconfig")
        self.target_collect_info("hciconfig")
        self.target_collect_info("lsmod")
        # Detect BT device status
        (status, output) = self.target.run('hciconfig hci0')
        self.assertEqual(status, 0, msg="Error messages: %s" % self.log)
