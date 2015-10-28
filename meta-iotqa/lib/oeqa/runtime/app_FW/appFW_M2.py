from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import get_files_dir
import os,json,glob,time

class AppFwTestForM2(oeRuntimeTest):

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

    """ App Framework testing for M2 rqts"""

    def _prepare_file_for_user(self, user_name, file_path):
        """ cp file to user home and change owner and smacklabel """
        file_name = os.path.basename(file_path)
        (status,output) = self.target.run("cp %s /home/%s" % (file_path, user_name))
        if status !=0 :
            return False 
        (status,output) = self.target.run("chown %s:%s /home/%s/%s" % 
                          (user_name, user_name, user_name, file_name))
        if status !=0 :
            return False 
        (status,output) = self.target.run("chsmack -a 'User::Home' /home/%s/%s" % 
                                         (self.test_app_user, file_name))
        if status !=0 :
            return False 
        return True

    def _installApp(self):
        """ install app """
        (status,output) = self.target.run("mkdir %s" % self.test_dir )
        test_app_paths = glob.glob(os.path.join(get_files_dir(), self.test_app_pkg))
        if test_app_paths :
            app_pkg_path = test_app_paths[-1]
        (status,output) = self.target.copy_to(app_pkg_path, self.test_dir)
        if status !=0 :
            return False 
        (status,output) = self.target.run("su -l %s -c 'iotpm -L | grep %s'" % 
                                         (self.test_app_user,self.test_app_name))
        if status == 0 :
            return True
        else:
            app_user_pkg_paths = glob.glob(os.path.join(get_files_dir(), self.test_app_user_pkg))
            if app_user_pkg_paths :
                app_user_pkg_path = app_user_pkg_paths[-1]
            self.target.copy_to(app_user_pkg_path, self.test_dir)
            (status,output) = self.target.run("rpm -ivh %s" % self.test_app_user_pkg_path)
            (status,output) = self.target.run("rpm -qa | grep %s" % self.test_app_user)
            if status !=0 :
                return False 

            self._prepare_file_for_user(self.test_app_user, self.test_app_pkg_path)
            
            (status,output) = self.target.run("su -l %s -c 'iotpm -i %s'" % 
                                             (self.test_app_user,self.test_app_pkg))
            if status !=0 :
                return False 
            else:
                return True
             
    def _uninstallApp(self):
        """ uninstall app """
        (status,output) = self.target.run("su -l %s -c 'iotpm -L | grep %s'" % 
                                         (self.test_app_user,self.test_app_name))
        if status == 0 :
            (status,output) = self.target.run("su -l %s -c 'iotpm -r %s'" % 
                                             (self.test_app_user,self.test_app_name))
            return status == 0
        else:
            print("App not installed")
            return False
    def _startApp(self):
        """ start app """
        if self._getPID(self.test_app_name):
            return True
        else:
            (status,output) = self.target.run("su -l %s -c 'iot-launch %s & '" % 
                                             (self.test_app_user,self.test_app_name))

            return self._getPID(self.test_app_name) != None

    def _stopApp(self):
        """ stop app """
        if not self._getPID(self.test_app_name):
            return False
        else:
            (status,output) = self.target.run("su -l %s -c 'iot-launch --stop %s'" % 
                                             (self.test_app_user,self.test_app_name))
            PID = self._getPID(self.test_app_name)
            if PID :
                print("Fail to stop PID %s" % PID)
                return False
            else:
                return True
        
    def _getPID(self,name):
        """ get process ID , return first one if has mutli-matched """
                
        (status,output) = self.target.run("ps | grep -vE 'grep|sh -c' | grep '%s'"  % name)
        (status,output) = self.target.run("ps | grep -vE 'grep|sh -c' | grep '%s' | awk 'NR==1 {print $1}'" % name)
        if status == 0 and output:
             return output
        else:
             return None

    def _list_app_not_run(self,cmd):
        """  list app not rung"""
        self.assertTrue(self._installApp(),'fail to install app')
        (status,output) = self.target.run("su -l %s -c '%s'" % (self.test_app_user,cmd))
        self.assertTrue(status == 0 and self.test_app_name in output, "fail to list all app")

    def _list_app_running(self,cmd):

        """  list app running """
        self.assertTrue(self._installApp(),'fail to install app')
        self.assertTrue(self._startApp(),"fail to start app")
        (status,output) = self.target.run("su -l %s -c '%s'" % (self.test_app_user,cmd))
        self.assertTrue(status == 0 and self.test_app_name in output, "fail to list running app")
         
    def test_list_all_app_by_C_API(self):
        """ test all app can be listed by C API """
        cmd = "iot-app-list -a" 
        self._list_app_not_run(cmd)

    def test_list_running_app_by_C_API(self):
        """ test running app can be listed by C API """
        cmd = "iot-app-list -r" 
        self._list_app_running(cmd)

    def _prepare_list_program(self,p):
        """ prepare list program """
        self.target.copy_to(os.path.join(os.path.dirname(__file__), "files", p),self.test_dir)
        list_app = os.path.join(self.test_dir,p) 
        self._prepare_file_for_user(self.test_app_user,list_app)

    def test_list_all_app_by_python_API(self):
        """ test all app can be listed by Python API """
        self._prepare_list_program(self.list_app_python)
        cmd = "python %s" % self.list_app_python
        self._list_app_not_run(cmd)

    def test_list_running_app_by_python_API(self):
        """ test running app can be listed by Python API """
        self._prepare_list_program(self.list_app_python)
        cmd = "python %s -r" % self.list_app_python
        self._list_app_running(cmd)

    def test_list_all_app_by_node_API(self):
        """ test all app can be listed by Node API """
        self._prepare_list_program(self.list_app_node)
        cmd = "node %s %s -a" % (self.list_app_node, self.node_lib_file) 
        self._list_app_not_run(cmd)

    def test_list_running_app_by_node_API(self):
        """ test running app can be listed by Node API """
        self._prepare_list_program(self.list_app_node)
        cmd = "node %s %s -r" % (self.list_app_node, self.node_lib_file) 
        self._list_app_running(cmd)

    def test_app_start(self):
        """ test app start successfuly """ 
        self.assertTrue(self._installApp(),'fail to install app')
        self.assertTrue(self._startApp(),"fail to start app")

    def test_app_stop(self):
        """ test app stop successfuly """ 
        self.assertTrue(self._installApp(),'fail to install app')
        self.assertTrue(self._startApp(),"fail to start app")
        self.assertTrue(self._stopApp(),"fail to stop app")

    def test_app_restart(self):
        """ test app re-start successfuly """ 
        self.assertTrue(self._installApp(),'fail to install app')
        self.assertTrue(self._startApp(),"fail to start app")
        self.assertTrue(self._stopApp(),"fail to stop app")
        self.assertTrue(self._startApp(),"fail to re-start app")

    def test_app_restop(self):
        """ test app re-stop successfuly """ 
        self.assertTrue(self._installApp(),'fail to install app')
        self.assertTrue(self._startApp(),"fail to start app")
        self.assertTrue(self._stopApp(),"fail to stop app")
        self.assertTrue(self._startApp(),"fail to start app")
        self.assertTrue(self._stopApp(),"fail to re-stop app")

    def test_appfw_security_app_info(self):
        """ test appfw has security enabled of app info """
        self.assertTrue(self._installApp(),'fail to install app')
        (status,output) = self.target.run("sqlite3 %s 'select * from app' " % self.security_db_file)
        self.assertTrue(self.test_app_name in output,"No app info found in security DB")

    def test_appfw_security_privileges(self):
        """ test appfw has security enabled of privileges """
        self.assertTrue(self._installApp(),'fail to install app')
        (status,output) = self.target.run("cat %s " % self.app_manifest_file)
        manifest_string = output.replace("\n","").replace(" ","")
        app_manifest_privileges = json.loads(manifest_string)[0]['privileges']
        (status,output) = self.target.run("sqlite3 %s 'select * from app_privilege_view' | grep '%s'" % 
                                         (self.security_db_file,self.test_app_name))
        for p in app_manifest_privileges :
             self.assertTrue(p in output,"No privilege %s found in security DB" % p)
             
    def test_app_Impersonation(self):
        """ test app test_App_Impersonation """
        self.assertTrue(self._installApp(),'fail to install app')
        self.assertTrue(self._startApp(),"fail to start app")
        PID = self._getPID(self.test_app_name)
        (status,smacklabel) = self.target.run("cat /proc/%s/attr/current" % PID)
        (status,UID) = self.target.run("id -u %s" % self.test_app_user) 
        self.assertTrue(UID in smacklabel and self.test_app_name in smacklabel) 
        
 
    def test_app_install(self):
        ''' test app installation '''
        self.assertTrue(self._installApp(),'fail to install app')

    def test_app_uninstall(self):
        ''' test app uninstallation '''
        self.assertTrue(self._installApp(),'fail to install app')
        self.assertTrue(self._uninstallApp(),'fail to uninstall app')

    def test_app_reinstall(self):
        ''' test app reinstall'''
        self.assertTrue(self._installApp(),'fail to install app')
        self.assertTrue(self._uninstallApp(),'fail to uninstall app')
        self.assertTrue(self._installApp(),'fail to reinstall app')

    def test_app_reuninstall(self):
        ''' test app re-uninstall'''
        self.assertTrue(self._installApp(),'fail to install app')
        self.assertTrue(self._uninstallApp(),'fail to uninstall app')
        self.assertTrue(self._installApp(),'fail to install app')
        self.assertTrue(self._uninstallApp(),'fail to re-uninstall app')
    
    def tearDown(self):
        ''' kill app if exists ''' 
        PID = self._getPID(self.test_app_name)
        if PID : 
            self.target.run("kill -9 %s" % PID)
            time.sleep(10)
        
