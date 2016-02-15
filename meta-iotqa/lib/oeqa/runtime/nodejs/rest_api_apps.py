"""
@file rest_api_apps.py
"""

##
# @addtogroup nodejs nodejs
# @brief This is nodejs component
# @{
# @addtogroup rest_api_apps rest_api_apps
# @brief This is rest_api_apps module
# @{
##

import os
import glob
import time
import json
import subprocess

from oeqa.oetest import oeRuntimeTest
from oeqa.utils.decorators import tag
from oeqa.utils.helper import get_files_dir


@tag(TestType='EFT', FeatureID='IOTOS-343')
class RESTAPIAppTest(oeRuntimeTest):
    """
    @class RESTAPIAppTest
    """

    test_dir = os.path.join(os.sep,"opt","appfw_test")
    list_app_python = "list-apps.py"
    list_app_node = "list-apps.js"
    node_lib_file = "/usr/lib/node_modules/iot/iot-appfw.node"
    test_app_pkg = "appfwTestApp-1.0.0*.rpm"
    test_app_user_pkg = "appfwtest-user-1.0.0*.rpm"
    test_app_name = "appfwTestApp"
    test_app_user = "appfwtest"
    test_app_pkg_path = os.path.join(test_dir,test_app_pkg)
    test_app_user_pkg_path = os.path.join(test_dir,test_app_user_pkg)
    app_manifest_file = "/usr/share/iot/users/%s/%s.manifest" % (test_app_user,test_app_name)
    security_db_file = "/usr/dbspace/.security-manager.db"

    rest_api_home = "/usr/lib/node_modules/iot-rest-api-server"
    rest_api_log = "/tmp/rest_api_server.log"
    appId = "%s:%s" % (test_app_name, test_app_name)

    """ App Framework testing for M2 rqts"""

    @classmethod
    def _prepare_file_for_user(cls, user_name, file_path):
        """ cp file to user home and change owner and smacklabel 
        @fn _prepare_file_for_user
        @param cls
        @param  user_name
        @param  file_path
        @return
        """
        file_name = os.path.basename(file_path)
        (status,output) = cls.tc.target.run("cp %s /home/%s" % (file_path, user_name))
        if status !=0 :
            return False 
        (status,output) = cls.tc.target.run("chown %s:%s /home/%s/%s" % 
                          (user_name, user_name, user_name, file_name))
        if status !=0 :
            return False 
        (status,output) = cls.tc.target.run("chsmack -a 'User::Home' /home/%s/%s" % 
                                         (cls.test_app_user, file_name))
        if status !=0 :
            return False 
        return True


    @classmethod
    def _installApp(cls):
        """ install app 
        @fn _installApp
        @param cls
        @return
        """
        (status,output) = cls.tc.target.run("mkdir %s" % cls.test_dir)
        test_app_paths = glob.glob(os.path.join(get_files_dir(), cls.test_app_pkg))
        app_pkg_path = None
        if test_app_paths :
            app_pkg_path = test_app_paths[-1]
        assert app_pkg_path is not None, "No app rpm packages named like %s found!" % cls.test_app_pkg
        
        (status,output) = cls.tc.target.copy_to(app_pkg_path, cls.test_dir)
        if status !=0 :
            return False 
        (status,output) = cls.tc.target.run("su -l %s -c 'iotpm -L | grep %s'" % 
                                         (cls.test_app_user,cls.test_app_name))
        if status == 0 :
            return True
        else:
            app_user_pkg_paths = glob.glob(os.path.join(get_files_dir(), cls.test_app_user_pkg))
            if app_user_pkg_paths :
                app_user_pkg_path = app_user_pkg_paths[-1]
            cls.tc.target.copy_to(app_user_pkg_path, cls.test_dir)
            (status,output) = cls.tc.target.run("rpm -ivh %s" % cls.test_app_user_pkg_path)
            (status,output) = cls.tc.target.run("rpm -qa | grep %s" % cls.test_app_user)
            if status !=0 :
                return False 

            cls._prepare_file_for_user(cls.test_app_user, cls.test_app_pkg_path)
            
            (status,output) = cls.tc.target.run("su -l %s -c 'iotpm -i %s'" % 
                                             (cls.test_app_user, cls.test_app_pkg))
            if status !=0 :
                return False 
            else:
                return True


    @classmethod             
    def _uninstallApp(cls):
        """ uninstall app 
        @fn _uninstallApp
        @param cls
        @return
        """
        (status,output) = cls.tc.target.run("su -l %s -c 'iotpm -L | grep %s'" % 
                                         (cls.test_app_user, cls.test_app_name))
        if status == 0 :
            (status,output) = cls.tc.target.run("su -l %s -c 'iotpm -r %s'" % 
                                             (cls.test_app_user, cls.test_app_name))
            return status == 0
        else:
            print("App not installed")
            return False


    @classmethod
    def _startApp(cls):
        """ start app 
        @fn _startApp
        @param cls
        @return
        """
        if cls._getPID(cls.test_app_name):
            return True
        else:
            (status,output) = cls.tc.target.run("su -l %s -c 'iot-launch %s & '" % 
                                             (cls.test_app_user, cls.test_app_name))
            return cls._getPID(cls.test_app_name) != None


    @classmethod
    def _stopApp(cls):
        """ stop app 
        @fn _stopApp
        @param cls
        @return
        """
        if not cls._getPID(cls.test_app_name):
            return False
        else:
            (status,output) = cls.tc.target.run("su -l %s -c 'iot-launch --stop %s'" % 
                                             (cls.test_app_user, cls.test_app_name))

            PID = cls._getPID(cls.test_app_name)
            if PID :
                print("Fail to stop PID %s" % PID)
                return False
            else:
                return True
        

    @classmethod
    def _getPID(cls,name):
        """ get process ID , return first one if has mutli-matched 
        @fn _getPID
        @param cls
        @param name
        @return
        """
        (status,output) = cls.tc.target.run("ps | grep '%s'"  % name)
        (status,output) = cls.tc.target.run("ps | grep '%s' | awk 'NR==1 {print $1}'" % name)
        if status == 0 and output:
             return output
        else:
             return None


    def _run_curl_cmd(self, method, path, appId = None):
        '''Send HTTP request via curl command tool, please disable all the proxy configration.
        @fn _run_curl_cmd
        @param self
        @param  method
        @param  path
        @param  appId 
        @return
        '''
        if appId:
            apps_install = appId
        else:
            apps_install = ''
        curl_cmd = ['curl', '-X', method, '--noproxy', '"*"', '-w', '%{http_code}', '--no-buffer', 'http://%s:8000/api/%s%s' % (self.target.ip, path, apps_install)]
        p = subprocess.Popen(curl_cmd, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
        p.wait()

        ret = p.returncode
        output = p.stdout.read()

        return (ret, output)


    @classmethod
    def _launch_rest_api_server(cls):
        '''Launch the REST API server
        @fn _launch_rest_api_server
        @param cls
        @return
        '''
        (_, output) = cls.tc.target.run("ps | grep -v grep | grep 'node index.js'")
        if not 'node index.js' in output:
            print('starting rest api server...')
            cls.tc.target.run("su -l %s -c 'cd %s;node index.js > %s 2>&1 &'" %
                         (cls.test_app_user, cls.rest_api_home, cls.rest_api_log))
            time.sleep(20)


    @classmethod
    def _stop_rest_api_server(cls):
        '''Kill the node index.js process and remove the test user
        @fn _stop_rest_api_server
        @param cls
        @return
        '''
        (_, pid) = cls.tc.target.run("ps | grep -v grep | grep 'node index.js' | awk '{print $1}'")
        if pid.strip():
            print('stopping rest api server...')
            cls.tc.target.run('kill %s' % pid.strip())
        else:
            print('rest api server is off.')       


    @classmethod
    def setUpClass(cls):
        '''Make sure the app is installed before running the test cases.
        @fn setUpClass
        @param cls
        @return
        '''
        cls._installApp()
        cls._launch_rest_api_server()
        cls._stopApp()

        
    @classmethod
    def tearDownClass(cls):
        '''Clean work, run only once
        @fn tearDownClass
        @param cls
        @return
        '''
        cls._stop_rest_api_server()


    def tearDown(self):
        '''Always stop the running apps before running the next test case.
        @fn tearDown
        @param self
        @return
        '''
        self._stopApp()


    def show_ps_node(self):
        '''See whether the rest api server is still on
        @fn show_ps_node
        @param self
        @return
        '''
        print('\n' + '#' * 80)
        (_, output) = self.target.run('ps | grep node')
        print(output)
        print('#' * 80)

    def show_ouput(self, output):
        """
        @fn show_ouput
        @param self
        @param  output
        @return
        """
        print('\n' + '*' * 80)
        print(output)
        print('*' * 80)


    def get_target_running_apps(self):
        '''Get the running apps of target devices.
        @fn get_target_running_apps
        @param self
        @return
        '''
        (returncode, output) = self.target.run("su -l %s -c'/usr/bin/iot-app-list -r'" % self.test_app_user)
    
        return (returncode, output)


    def test_api_apps(self):
        '''A complete usecase to test /api/apps with GET/POST/DELETE/PUT methods
        @fn test_api_apps
        @param self
        @return
        '''
        # No running apps.
        (_, output) = self.get_target_running_apps()
        self.show_ouput(output)
        ##
        # TESTPOINT: #1, test_api_apps
        #
        self.assertTrue('Got list of 0 applications' in output)

        # Now all the apps running
        print('\ntesting POST to start all installed apps...')
        (returncode, output) = self._run_curl_cmd('POST', 'apps')
        self.show_ouput(output)
        ##
        # TESTPOINT: #2, test_api_apps
        #
        self.assertTrue(output.strip().endswith('200'))
        (_, output) = self.get_target_running_apps()
        self.show_ouput(output)
        ##
        # TESTPOINT: #3, test_api_apps
        #
        self.assertTrue(('appid: %s' % self.appId) in output)
        print('\ntesting POST passed')   

        # Get the running apps list
        print('\ntesting GET to list all running apps...')
        (returncode, output) = self._run_curl_cmd('GET', 'apps')
        self.show_ouput(output)
        ##
        # TESTPOINT: #4, test_api_apps
        #
        self.assertTrue(output.strip().endswith('200'))
        ##
        # TESTPOINT: #5, test_api_apps
        #
        self.assertTrue(('%s' % self.appId) in output)
        (_, output) = self.get_target_running_apps()
        self.show_ouput(output)
        ##
        # TESTPOINT: #6, test_api_apps
        #
        self.assertTrue(('appid: %s' % self.appId) in output)
        print('\ntesting GET passed')     

        # Now restart all the running apps
        print('\ntesting PUT to restart all running apps...')
        (_, output) = self._run_curl_cmd('PUT', 'apps')
        self.show_ouput(output)
        ##
        # TESTPOINT: #7, test_api_apps
        #
        self.assertTrue(output.strip().endswith('200'))
        (_, output) = self.get_target_running_apps()
        self.show_ouput(output)
        ##
        # TESTPOINT: #8, test_api_apps
        #
        self.assertTrue(('appid: %s' % self.appId) in output)
        print('\ntesting PUT passed')             

        # # Now stop all the running apps
        print('\ntesting DELETE all running apps ...')
        (_, output) = self._run_curl_cmd('DELETE', 'apps')
        self.show_ouput(output)
        ##
        # TESTPOINT: #9, test_api_apps
        #
        self.assertTrue(output.strip().endswith('200'))        
        (_, output) = self.get_target_running_apps()
        self.show_ouput(output)
        ##
        # TESTPOINT: #10, test_api_apps
        #
        self.assertTrue('Got list of 0 applications' in output)
        print('\ntesting DELETE passed')
            

    def test_api_apps_with_appid(self):
        '''A complete usecase to test /api/apps/<appId> with GET/POST/DELETE/PUT methods
        @fn test_api_apps_with_appid
        @param self
        @return
        '''
        self._startApp()

        # Get the running app
        print('\ntesting GET to list single app...')
        (returncode, output) = self._run_curl_cmd('GET', 'apps', '/%s' % self.appId)
        self.show_ouput(output)               
        ##
        # TESTPOINT: #1, test_api_apps_with_appid
        #
        self.assertTrue(output.strip().endswith('200'))
        ##
        # TESTPOINT: #2, test_api_apps_with_appid
        #
        self.assertTrue(('%s' % self.appId) in output)
        (_, output) = self.get_target_running_apps()
        self.show_ouput(output)
        ##
        # TESTPOINT: #3, test_api_apps_with_appid
        #
        self.assertTrue(('appid: %s' % self.appId) in output)
        print('\ntesting GET passed')        

        # Now restart the running app
        print('\ntesting PUT to restart single app...')
        (_, output) = self._run_curl_cmd('PUT', 'apps', '/%s' % self.appId)
        self.show_ouput(output)        
        ##
        # TESTPOINT: #4, test_api_apps_with_appid
        #
        self.assertTrue(output.strip().endswith('200'))
        (_, output) = self.get_target_running_apps()
        self.show_ouput(output)
        ##
        # TESTPOINT: #5, test_api_apps_with_appid
        #
        self.assertTrue(('appid: %s' % self.appId) in output)
        print('\ntesting PUT passed')

        # Now stop the running app
        print('\ntesting DELETE to stop single app...')
        (_, output) = self._run_curl_cmd('DELETE', 'apps', '/%s' % self.appId)
        self.show_ouput(output)       
        ##
        # TESTPOINT: #6, test_api_apps_with_appid
        #
        self.assertTrue(output.strip().endswith('200'))
        (_, output) = self.get_target_running_apps()
        self.show_ouput(output)
        ##
        # TESTPOINT: #7, test_api_apps_with_appid
        #
        self.assertTrue('Got list of 0 applications' in output)
        print('\ntesting DELETE passed')

        # Now start the single app
        print('\ntesting POST to start single app...')
        (returncode, output) = self._run_curl_cmd('POST', 'apps', '/%s' % self.appId)
        self.show_ouput(output)
        ##
        # TESTPOINT: #8, test_api_apps_with_appid
        #
        self.assertTrue(output.strip().endswith('200'))
        (_, output) = self.get_target_running_apps()
        self.show_ouput(output)
        ##
        # TESTPOINT: #9, test_api_apps_with_appid
        #
        self.assertTrue(('appid: %s' % self.appId) in output)
        print('\ntesting POST passed')

##
# @}
# @}
##

