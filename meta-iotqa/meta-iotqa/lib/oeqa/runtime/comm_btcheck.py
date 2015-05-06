from oeqa.oetest import oeRuntimeTest

class CommBluetoothTest(oeRuntimeTest):
    '''Bluetooth device check'''
    def test_comm_btcheck(self):
        '''check bluetooth device'''
        # un-block software rfkill lock
        self.target.run('rfkill unblock all')
        # Detect BT device status
        (status, output) = self.target.run('hciconfig hci0')
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
