from oeqa.oetest import oeRuntimeTest
from oeqa.utils.decorators import skipUnlessPassed
import time

class AppFwTest(oeRuntimeTest):

    """ App Framework testing """

    def _getPID(self,name):
        """ get process ID , return first one if has mutli-matched """
                
        (status,output) = self.target.run("ps | grep -v grep | grep %s | awk 'NR==1 {print $1}'" % name)
        if status == 0 and output:
             return output
        else:
             return None
        
    def test_appFW_install_pkg_during_img_creation(self):
        """ test example-app and exmaple-session are installed in image """

        (chk_example_app,output) = self.target.run("rpm -qa | grep -i example-app")

        (chk_example_session,output) = self.target.run("rpm -qa | grep -i example-session")

        self.assertTrue(chk_example_app == 0 and chk_example_session == 0 ,
                        "example-app and example-session are not integreated in image")

    @skipUnlessPassed('oeqa.runtime.app_FW.appFW.AppFwTest.test_appFW_install_pkg_during_img_creation')
    def test_appFW_start_app_on_device_startup(self): 
        """ test example-app is started on device startup """
        
        self.assertTrue(self._getPID("example-app") != None , "app not running on device startup")

    @skipUnlessPassed('oeqa.runtime.app_FW.appFW.AppFwTest.test_appFW_install_pkg_during_img_creation')
    def test_appFW_app_running_with_Dedicated_User(self):
        """ test app running with dedicated user """ 

        (status,output) = self.target.run("ps | grep -v grep | grep example-app | awk 'NR==1 {print $2}'" )

        self.assertEqual( status, 0, "Fail to run ps" )
       
        self.assertTrue('example' in output , "Not found app running with dedicated user")
         
    @skipUnlessPassed('oeqa.runtime.app_FW.appFW.AppFwTest.test_appFW_install_pkg_during_img_creation')
    def test_appFW_stop_app_service(self):
        """ test stop app and service """ 

        (status,output) = self.target.run("systemctl stop example-corp")
        time.sleep(3)
        self.assertTrue(status == 0 and self._getPID("example-app") == None , output)

    @skipUnlessPassed('oeqa.runtime.app_FW.appFW.AppFwTest.test_appFW_install_pkg_during_img_creation')
    def test_appFW_start_app_ondemand(self):
        
        old_pid = self._getPID("example-app")
        if not old_pid:
            (status,output) = self.target.run("systemctl start example-corp")
            self.assertEqual(status,0,output)
            old_pid = self._getPID("example-app")

        (status,output) = self.target.run("systemctl stop example-corp")
        self.assertEqual(status,0,output)
        time.sleep(3)
        (status,output) = self.target.run("systemctl start example-corp")
        self.assertEqual(status,0,output)
        new_pid = self._getPID("example-app") 
        self.assertTrue(old_pid != new_pid, "restart app failed")       
        
    @skipUnlessPassed('oeqa.runtime.app_FW.appFW.AppFwTest.test_appFW_install_pkg_during_img_creation')
    def test_appFW_app_event_TERM(self):
        """ test basic app event SIGTERM """

        pid = self._getPID("example-app")
        if not pid:
            (status,output) = self.target.run("systemctl start example-corp")
            self.assertEqual(status,0,output)
        else:
            (status,output) = self.target.run("kill -TERM %s" % pid)
             
        self.assertTrue(self._getPID("example-app") == None , "App fail to respond TERM signal")

    def tearDown(self):
        self.target.run("systemctl start example-corp")
        time.sleep(3)
