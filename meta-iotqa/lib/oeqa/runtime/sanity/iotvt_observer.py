import os
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import get_files_dir

class IOtvtClient(oeRuntimeTest):
    '''Iotivity client set observer'''
    def test_iotvt_observer(self):
        '''Prepare test binaries to image'''
        (status, output) = self.target.run('mkdir -p /opt/iotivity-test/apps/iotivity-test/')
        (status, output) = self.target.run("ps | grep servertest | awk '{print $1}' | xargs kill -9")
        (status, output) = self.target.copy_to(os.path.join(get_files_dir(),
                          'servertest'), "/opt/iotivity-test/apps/iotivity-test/")
        (status, output) = self.target.copy_to(os.path.join(get_files_dir(),
                          'clienttest'), "/opt/iotivity-test/apps/iotivity-test/")

        '''start iotivity server to register a new resource'''
        reg_cmd = "/opt/iotivity-test/apps/iotivity-test/servertest > /dev/null 2>&1 &"
        (status, output) = self.target.run(reg_cmd)
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
        
        '''client starts to set observer'''
        client_cmd = "/opt/iotivity-test/apps/iotivity-test/clienttest Observer"
        (status, output) = self.target.run(client_cmd)
        self.assertEqual(status, 0, msg="Error messages: %s" % output)
