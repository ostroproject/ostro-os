import os

from oeqa.oetest import oeRuntimeTest

class IOtvtClient(oeRuntimeTest):
    '''Iotivity client set resource state'''
    def test_iotvt_setstate(self):
        '''Prepare test binaries to image'''
        (status, output) = self.target.run('mkdir -p /opt/iotivity-test/apps/iotivity-test/')
        (status, output) = self.target.run('ls /opt/iotivity-test/apps/iotivity-test/servertest')
        if status != 0:
            (status,output) = self.target.copy_to(os.path.join(oeRuntimeTest.tc.filesdir,
                          'servertest'), "/opt/iotivity-test/apps/iotivity-test/")
            (status,output) = self.target.copy_to(os.path.join(oeRuntimeTest.tc.filesdir,
                          'clienttest'), "/opt/iotivity-test/apps/iotivity-test/")

        '''start iotivity server to register a new resource'''
        (status, output) = self.target.run("ps | grep servertest | awk '{print $1}' | xargs kill -9")
        reg_cmd = "/opt/iotivity-test/apps/iotivity-test/servertest > /dev/null 2>&1 &"
        (status, output) = self.target.run(reg_cmd)
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
        
        '''client starts to set resource state'''
        client_cmd = "/opt/iotivity-test/apps/iotivity-test/clienttest SetState"
        (status, output) = self.target.run(client_cmd)
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
