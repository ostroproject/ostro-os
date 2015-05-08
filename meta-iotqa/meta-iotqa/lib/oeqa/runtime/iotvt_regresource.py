from oeqa.oetest import oeRuntimeTest

class IOtvtServer(oeRuntimeTest):
    '''Iotivity server registers a new resource'''
    def test_iotvt_regresource(self):
        '''start iotivity server to register a new resource'''
        reg_cmd = "/opt/iotivity-test/apps/iotivity-test/servertesti > /dev/null 2>&1 &"
        (status, output) = self.target.run(reg_cmd)
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
