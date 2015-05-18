import os
from oeqa.oetest import oeRuntimeTest

class IOtvtClient(oeRuntimeTest):
    '''Iotivity client get resource state'''
    def test_iotvt_getstate(self):
        '''Prepare test binaries to image'''
        (status, output) = self.target.run('mkdir -p /opt/iotivity-test/apps/iotivity-test/')
        (status, output) = self.target.run('ls /opt/iotivity-test/apps/iotivity-test/servertest')
        if status != 0:
            (status,output) = self.target.copy_to(os.path.join(os.path.dirname(__file__),'files',
                          'servertest'), "/opt/iotivity-test/apps/iotivity-test/")
        (status, output) = self.target.run('ls /opt/iotivity-test/apps/iotivity-test/clienttest')
        if status != 0:
            (status,output) = self.target.copy_to(os.path.join(os.path.dirname(__file__),'files',
                          'clienttest'), "/opt/iotivity-test/apps/iotivity-test/")

        '''start iotivity server to register a new resource'''
        (status, output) = self.target.run("ps | grep servertest | awk '{print $1}' | xargs kill -9")
        reg_cmd = "/opt/iotivity-test/apps/iotivity-test/servertest > /dev/null 2>&1 &"
        (status, output) = self.target.run(reg_cmd)
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
        
        '''client starts to get resource state'''
        client_cmd = "/opt/iotivity-test/apps/iotivity-test/clienttest GetState"
        (status, output) = self.target.run(client_cmd)
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
