import os
import time
import string
import subprocess
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import shell_cmd_timeout
from oeqa.utils.helper import get_files_dir
from oeqa.utils.helper import tag

@tag(TestType="Functional Positive")
class IOtvtClient(oeRuntimeTest):
    @classmethod
    def setUpClass(cls):
        '''Put files onto target and do WiFi connection'''
        # Prepare test binaries to image
        (status, output) = cls.tc.target.run('mkdir -p /opt/iotivity-test/apps/iotivity-test/')
        (status, output) = cls.tc.target.run("ps | grep servertest | awk '{print $1}' | xargs kill -9")
        # clienttest needs to be killed twice
        (status, output) = cls.tc.target.run("ps | grep clienttest | awk '{print $1}' | xargs kill -9")
        (status, output) = cls.tc.target.run("ps | grep clienttest | awk '{print $1}' | xargs kill -9")
        print get_files_dir()
        (status, output) = cls.tc.target.copy_to(os.path.join(get_files_dir(),
                          'servertest'), "/opt/iotivity-test/apps/iotivity-test/")
        (status, output) = cls.tc.target.copy_to(os.path.join(get_files_dir(),
                          'clienttest'), "/opt/iotivity-test/apps/iotivity-test/")
        #start iotivity server to register a new resource
        (status, output) = cls.tc.target.run('/opt/iotivity-test/apps/iotivity-test/servertest > /tmp/output &')
        #server = os.path.join(os.path.dirname(__file__), "files/servertest > /dev/null 2>&1") 
        #subprocess.Popen(server, shell=True)

    @classmethod
    def tearDownClass(cls):
        '''kill servertest on Target'''
        (status, output) = cls.tc.target.run("killall servertest")
        #shell_cmd_timeout("ps -ef | grep servertest | awk '{print $2}' | xargs kill -9", timeout=200)        

    @tag(FeatureID="IOTOS-498")
    def test_iotvt_findresource(self):
        '''Target finds resource, registered by Host'''
        client_cmd = "/opt/iotivity-test/apps/iotivity-test/clienttest FindResource"
        (status, output) = self.target.run(client_cmd)
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

    @tag(FeatureID="IOTOS-498")
    def test_iotvt_getstate(self):
        '''Target starts to get resource state'''
        client_cmd = "/opt/iotivity-test/apps/iotivity-test/clienttest GetState"
        (status, output) = self.target.run(client_cmd)
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

    @tag(FeatureID="IOTOS-498")
    def test_iotvt_observer(self):
        '''Target starts to set observer'''
        client_cmd = "/opt/iotivity-test/apps/iotivity-test/clienttest Observer"
        (status, output) = self.target.run(client_cmd)
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

    @tag(FeatureID="IOTOS-498")
    def test_iotvt_setstate(self):
        '''Target starts to set resource state'''
        client_cmd = "/opt/iotivity-test/apps/iotivity-test/clienttest SetState"
        (status, output) = self.target.run(client_cmd)
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

    @tag(FeatureID="IOTOS-498")
    def test_iotvt_regresource(self):
        '''Target starts servertest. And after several seconds, it should not crash'''
        # ensure there is no servertest running background
        #(status, output) = self.target.run("ps | grep servertest | awk '{print $1}' | xargs kill -9")
        # start the server
        #(status, output) = self.target.run('/opt/iotivity-test/apps/iotivity-test/servertest &')
        #self.assertEqual(status, 0, msg="Error messages: %s" % output)
        time.sleep(5)
        # check if servertest is there
        (status, output) = self.target.run('ps | grep servertest -c')
        number = string.atoi(output)
        self.assertEqual(number, 3, msg="Error messages: %s" % output)
