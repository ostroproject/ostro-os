from oeqa.oetest import oeRuntimeTest
from oeqa.utils.decorators import skipUnlessPassed
from oeqa.utils.helper import get_files_dir
import time,os

class AppFwTestPython(oeRuntimeTest):

    test_dir = os.path.join(os.sep,"opt","appfw_test")
    catch_app = 'appfw-python-event-catch.py'
    send_app = 'appfw-python-event-send.py'
    catch_app_path = os.path.join(test_dir,catch_app)
    send_app_path = os.path.join(test_dir,send_app)
    appfw_test_log = os.path.join(test_dir,'appfw_test.log')

    """ App Framework testing """

    def _getPID(self,name):
        """ get process ID , return first one if has mutli-matched """
                
        (status,output) = self.target.run("ps | grep -vE 'grep|sh -c' | grep '%s' | awk 'NR==1 {print $1}'" % name)
        if status == 0 and output:
             return output
        else:
             return None

    def setUp(self):
        """ Initial testing folder , check appfw python module and start launcher daemon """

        (status,output) = self.target.run("mkdir %s" % self.test_dir )
        self.target.copy_to(os.path.join(os.path.dirname(__file__), "files", self.catch_app),self.test_dir)
        self.target.copy_to(os.path.join(os.path.dirname(__file__), "files", self.send_app),self.test_dir)
        (status,output) = self.target.run("python -c 'import appfw'")
        self.assertTrue(status==0 ,"No python appfw module in image")
        (status,output) = self.target.run("systemctl start iot-launch")
        self.assertTrue(self._getPID("iot-launch") != None)
         
        
    def test_appFW_Python_SIGTERM(self):
        """ test python app respond to SIGTERM """

        (status,output) = self.target.run("python %s -s -d & " % self.catch_app_path)

        PID = self._getPID(self.catch_app)
        self.assertTrue(PID!=None, 'unable to get PID of catch app')
        (status,output) = self.target.run("kill -TERM %s " % PID)
    
        time.sleep(5)
        expected_output = "Received a SIGTERM, quitting mainloop..."
        (status,catch_app_output) = self.target.run("cat %s | grep '%s' " % (self.appfw_test_log , expected_output))
        
        self.assertTrue(self._getPID(self.catch_app) == None and status == 0 ,
                        "Fail to terminate python app")

    def test_appFW_Python_SIGHUP(self):
        """ test python app respond to SIGHUP """

        (status,output) = self.target.run("python %s -s -d & " % self.catch_app_path)

        PID = self._getPID(self.catch_app)
        self.assertTrue(PID!=None, 'unable to get PID of catch app')
        (status,output) = self.target.run("kill -HUP %s " % PID)
        time.sleep(5)
        expected_output = "Received SIGHUP, doing nothing..."
        (status,catch_app_output) = self.target.run("cat %s | grep '%s' " % (self.appfw_test_log , expected_output))
        
        self.assertTrue(self._getPID(self.catch_app) != None and status == 0 ,
                        "app not respond to SIGHUP")

    def _test_appFW_Python_Send_Receive_Event(self,cmd):
        """ test python app can send/receive events """

        (status,output) = self.target.run("python %s -s -e a,b,c -d  &" % self.catch_app_path)
        PID = self._getPID(self.catch_app)
        self.assertTrue(PID != None, 'unable to get PID of catch app')
        if 'PID' in cmd:
            cmd = cmd.replace('PID',PID)
        (status,output) = self.target.run(cmd)
        expected_outputs = [
                            "Received an event with event = a, data = {u'k': u'v'}",
                            "Received an event with event = b, data = {u'k': u'v'}",
                            "Received an event with event = c, data = {u'k': u'v'}",
                            ]
        for res in expected_outputs:
            (status,catch_app_output) = self.target.run(r"""cat %s | grep "%s" """ % (self.appfw_test_log, res))
            self.assertTrue(self._getPID(self.catch_app) != None and status == 0 ,
                        "Receive event %s fail" % res )
    
    def test_appFW_Python_Send_Recevie_Event_By_ProcessID(self):
        """ test python app can send/receive events by process ID"""

        command = r"""python %s -e a,b,c -D '{"k":"v"}' -p PID -dddd """ % (self.send_app_path)

        self._test_appFW_Python_Send_Receive_Event(command)

    def test_appFW_Python_Send_Recevie_Event_By_User(self):
        """ test python app can send/receive events by user"""
        
        command = r"""python %s -e a,b,c -D '{"k":"v"}' -u root -dddd """ % (self.send_app_path)

        self._test_appFW_Python_Send_Receive_Event(command)

    def test_appFW_Python_Send_Recevie_Event_By_Binary(self):
        """ test python app can send/receive events by binary"""
        
        command = r"""python %s -e a,b,c -D '{"k":"v"}' -b %s -dddd """ % (self.send_app_path, self.catch_app_path)

        self._test_appFW_Python_Send_Receive_Event(command)

    def test_appFW_Python_Send_Recevie_Event_Negative(self):
        """ test python app should not receive un-subscribed events """

        (status,output) = self.target.run("python %s -s -e a,b,c -d  &" % self.catch_app_path)
        
        PID = self._getPID(self.catch_app)
        self.assertTrue(PID!=None, 'unable to get PID of catch app')
        (status,output) = self.target.run(r"""python %s -e e,f,g -D '{"k":"v"}' -p %s -dddd """ % (self.send_app_path,PID))
        expected_outputs = [
                            "Received an event with event = e, data = {u'k': u'v'}",
                            "Received an event with event = f, data = {u'k': u'v'}",
                            "Received an event with event = g, data = {u'k': u'v'}",
                            ]
        for res in expected_outputs:
            (status,catch_app_output) = self.target.run(r"""cat %s | grep "%s" """ % (self.appfw_test_log, res))
            self.assertTrue(self._getPID(self.catch_app) != None and status !=0 ,
                        "Receive event %s fail" % res )

    def tearDown(self):
        """ Stop catch app , stop launcher daemon and clean up testing log """

        PID  = self._getPID(self.catch_app)
        if PID :
            self.target.run("kill -9 %s" % PID)
            time.sleep(2)
             

        self.target.run("systemctl stop iot-launch")
        (status,output) = self.target.run("rm -f %s" % self.appfw_test_log)
        time.sleep(2)
