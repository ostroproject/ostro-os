from oeqa.oetest import oeRuntimeTest
from oeqa.utils.decorators import skipUnlessPassed
import time

class AppFwTest(oeRuntimeTest):

    """ App Framework testing """

    def _getPID(self,name):
        """ get process ID , return first one if has mutli-matched """
                
        (status,output) = self.target.run("ps | grep -v grep | grep %s | awk 'NR==1 {print $1}'" % name)
        if status == 0 and output.strip():
             return output
        else:
             return None
        
    def test_appFW_install_pkg_during_img_creation(self):
        """ test example-app is pre-installed in image """

        (chk_example_app,output) = self.target.run("ls /home/iodine/apps_rw/example-app")

        self.assertTrue(chk_example_app == 0 ,
                        "example-app is not integreated in image")

    @skipUnlessPassed('oeqa.runtime.app_FW.appFW.AppFwTest.test_appFW_install_pkg_during_img_creation')
    def test_appFW_start_app_on_device_startup(self): 
        """ test example-app is started on device startup """
        time.sleep(12) 
        self.assertTrue(self._getPID("example-app") != None , "app not running on device startup")

    @skipUnlessPassed('oeqa.runtime.app_FW.appFW.AppFwTest.test_appFW_install_pkg_during_img_creation')
    def test_appFW_app_running_with_Dedicated_User(self):
        """ test app running with dedicated user """ 

        (status,output) = self.target.run("ps | grep -v grep | grep example-app | awk 'NR==1 {print $2}'" )

        self.assertEqual( status, 0, "Fail to run ps" )
       
        self.assertTrue('iodine' in output , "Not found app running with dedicated user")
         
    @skipUnlessPassed('oeqa.runtime.app_FW.appFW.AppFwTest.test_appFW_install_pkg_during_img_creation')
    def test_appFW_stop_app_service(self):
        """ test stop app and service """ 

        (status,output) = self.target.run("systemctl stop iodine-session")
        time.sleep(5)
        self.assertTrue(status == 0 and self._getPID("example-app") == None , output)

    @skipUnlessPassed('oeqa.runtime.app_FW.appFW.AppFwTest.test_appFW_install_pkg_during_img_creation')
    def test_appFW_start_app_ondemand(self):
        """ test start app ondemand """ 

        old_pid = self._getPID("example-app")
        if not old_pid:
            (status,output) = self.target.run("systemctl start iodine-session")
            self.assertEqual(status,0,output)
            time.sleep(12)
            old_pid = self._getPID("example-app")

        (status,output) = self.target.run("systemctl stop iodine-session")
        self.assertEqual(status,0,output)
        time.sleep(5)
        (status,output) = self.target.run("systemctl start iodine-session")
        time.sleep(12)
        self.assertEqual(status,0,output)
        new_pid = self._getPID("example-app") 
        self.assertTrue(new_pid != None , 'Fail to start example-app')   
        self.assertTrue(old_pid !=None and old_pid != new_pid, "restart app failed")       
        
    @skipUnlessPassed('oeqa.runtime.app_FW.appFW.AppFwTest.test_appFW_install_pkg_during_img_creation')
    def test_appFW_app_event_TERM(self):
        """ test basic app event SIGTERM """

        pid = self._getPID("example-app")
        self.assertTrue(pid != None , 'Not found example-app running')   
        (status,output) = self.target.run("kill -TERM %s" % pid)
        time.sleep(3)
        self.assertTrue(self._getPID("example-app") == None , "App fail to respond TERM signal")

    def tearDown(self):
        """ resume example session """
        if not self._getPID("example-app"):
            (status,output) = self.target.run("tlm-client -o --seat seat0")
            self.target.run("systemctl start iodine-session")
            time.sleep(12)
