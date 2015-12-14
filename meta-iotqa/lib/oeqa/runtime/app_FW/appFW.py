"""
@file appFW.py
"""

##
# @addtogroup app_FW app_FW
# @brief This is app_FW component
# @{
# @addtogroup appFW appFW
# @brief This is appFW module
# @{
##

from oeqa.oetest import oeRuntimeTest
from oeqa.utils.decorators import skipUnlessPassed
import time

class AppFwTest(oeRuntimeTest):
    """ App Framework testing 
    @class AppFwTest
    """


    def _getPID(self,name):
        """ get process ID , return first one if has mutli-matched 
        @fn _getPID
        @param self
        @param name
        @return
        """
                
        (status,output) = self.target.run("ps | grep -v grep | grep %s | awk 'NR==1 {print $1}'" % name)
        if status == 0 and output.strip():
             return output
        else:
             return None
        
    def test_appFW_install_pkg_during_img_creation(self):
        """ test example-app is pre-installed in image 
        @fn test_appFW_install_pkg_during_img_creation
        @param self
        @return
        """

        (chk_example_app,output) = self.target.run("ls /home/iodine/apps_rw/example-app")

        ##
        # TESTPOINT: #1, test_appFW_install_pkg_during_img_creation
        #
        self.assertTrue(chk_example_app == 0 ,
                        "example-app is not integreated in image")

    @skipUnlessPassed('oeqa.runtime.app_FW.appFW.AppFwTest.test_appFW_install_pkg_during_img_creation')
    def test_appFW_start_app_on_device_startup(self): 
        """ test example-app is started on device startup 
        @fn test_appFW_start_app_on_device_startup
        @param self
        @return
        """
        time.sleep(12) 
        ##
        # TESTPOINT: #1, test_appFW_start_app_on_device_startup
        #
        self.assertTrue(self._getPID("example-app") != None , "app not running on device startup")

    @skipUnlessPassed('oeqa.runtime.app_FW.appFW.AppFwTest.test_appFW_install_pkg_during_img_creation')
    def test_appFW_app_running_with_Dedicated_User(self):
        """ test app running with dedicated user 
        @fn test_appFW_app_running_with_Dedicated_User
        @param self
        @return
        """

        (status,output) = self.target.run("ps | grep -v grep | grep example-app | awk 'NR==1 {print $2}'" )

        ##
        # TESTPOINT: #1, test_appFW_app_running_with_Dedicated_User
        #
        self.assertEqual( status, 0, "Fail to run ps" )
       
        ##
        # TESTPOINT: #2, test_appFW_app_running_with_Dedicated_User
        #
        self.assertTrue('iodine' in output , "Not found app running with dedicated user")
         
    @skipUnlessPassed('oeqa.runtime.app_FW.appFW.AppFwTest.test_appFW_install_pkg_during_img_creation')
    def test_appFW_stop_app_service(self):
        """ test stop app and service 
        @fn test_appFW_stop_app_service
        @param self
        @return
        """

        (status,output) = self.target.run("systemctl stop iodine-session")
        time.sleep(5)
        ##
        # TESTPOINT: #1, test_appFW_stop_app_service
        #
        self.assertTrue(status == 0 and self._getPID("example-app") == None , output)

    @skipUnlessPassed('oeqa.runtime.app_FW.appFW.AppFwTest.test_appFW_install_pkg_during_img_creation')
    def test_appFW_start_app_ondemand(self):
        """ test start app ondemand 
        @fn test_appFW_start_app_ondemand
        @param self
        @return
        """

        old_pid = self._getPID("example-app")
        if not old_pid:
            (status,output) = self.target.run("systemctl start iodine-session")
            ##
            # TESTPOINT: #1, test_appFW_start_app_ondemand
            #
            self.assertEqual(status,0,output)
            time.sleep(12)
            old_pid = self._getPID("example-app")

        (status,output) = self.target.run("systemctl stop iodine-session")
        ##
        # TESTPOINT: #2, test_appFW_start_app_ondemand
        #
        self.assertEqual(status,0,output)
        time.sleep(5)
        (status,output) = self.target.run("systemctl start iodine-session")
        time.sleep(12)
        ##
        # TESTPOINT: #3, test_appFW_start_app_ondemand
        #
        self.assertEqual(status,0,output)
        new_pid = self._getPID("example-app") 
        ##
        # TESTPOINT: #4, test_appFW_start_app_ondemand
        #
        self.assertTrue(new_pid != None , 'Fail to start example-app')   
        ##
        # TESTPOINT: #5, test_appFW_start_app_ondemand
        #
        self.assertTrue(old_pid !=None and old_pid != new_pid, "restart app failed")       
        
    @skipUnlessPassed('oeqa.runtime.app_FW.appFW.AppFwTest.test_appFW_install_pkg_during_img_creation')
    def test_appFW_app_event_TERM(self):
        """ test basic app event SIGTERM 
        @fn test_appFW_app_event_TERM
        @param self
        @return
        """

        pid = self._getPID("example-app")
        ##
        # TESTPOINT: #1, test_appFW_app_event_TERM
        #
        self.assertTrue(pid != None , 'Not found example-app running')   
        (status,output) = self.target.run("kill -TERM %s" % pid)
        time.sleep(3)
        ##
        # TESTPOINT: #2, test_appFW_app_event_TERM
        #
        self.assertTrue(self._getPID("example-app") == None , "App fail to respond TERM signal")

    def tearDown(self):
        """ resume example session 
        @fn tearDown
        @param self
        @return
        """
        if not self._getPID("example-app"):
            (status,output) = self.target.run("tlm-client -o --seat seat0")
            self.target.run("systemctl start iodine-session")
            time.sleep(12)

##
# @}
# @}
##

