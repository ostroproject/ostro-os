import os
import string
import time
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import get_files_dir

class IOtvtServer(oeRuntimeTest):
    '''Iotivity server registers a new resource'''
    def test_iotvt_regresource(self):
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

        ''' after several seconds, the daemon should not crash'''
        time.sleep(5)
        (status, output) = self.target.run('ps | grep servertest -c')
        number = string.atoi(output)
        self.assertEqual(number, 3, msg="Error messages: %s" % output)
