from oeqa.oetest import oeRuntimeTest

class IOtvtClient(oeRuntimeTest):
    '''Iotivity client finds resource'''
    def test_iotvt_findresource(self):
        '''Prepare test binaries to image'''
        (status,output) = self.target.copy_to(os.path.join(oeRuntimeTest.tc.filesdir,
                          'servertest'), "/opt/iotivity-test/apps/iotivity-test/")
        (status,output) = self.target.copy_to(os.path.join(oeRuntimeTest.tc.filesdir,
                          'clienttest'), "/opt/iotivity-test/apps/iotivity-test/")

        '''start iotivity server to register a new resource'''
        reg_cmd = "/opt/iotivity-test/apps/iotivity-test/servertest > /dev/null 2>&1 &"
        (status, output) = self.target.run(reg_cmd)
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
        
        '''client starts to find resource'''
        client_cmd = "/opt/iotivity-test/apps/iotivity-test/clienttest FindResource"
        (status, output) = self.target.run(client_cmd)
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
