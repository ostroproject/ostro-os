import os
import time
import string
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import get_files_dir
from oeqa.utils.helper import shell_cmd_timeout
from oeqa.utils.helper import tag

@tag(TestType="Functional Positive", FeatureID="IOTOS-754")
class IOtvtIntegration(oeRuntimeTest):
    def presence_check(self, para):
        '''this is a function used by presence test'''
        # ensure env is clean
        self.target.run("killall presenceserver")        
        self.target.run("killall presenceclient")        
        # start server
        server_cmd = "/opt/iotivity/examples/resource/cpp/presenceserver > /tmp/svr_output &"
        (status, output) = self.target.run(server_cmd)
        time.sleep(1)
        # start client to get info
        client_cmd = "/opt/iotivity/examples/resource/cpp/presenceclient -t %d > /tmp/output &" % para
        self.target.run(client_cmd)
        time.sleep(15)
        (status, output) = self.target.run("cat /tmp/output | grep 'Received presence notification from' -c")
        self.target.run("killall presenceserver")        
        self.target.run("killall presenceclient")
        return string.atoi(output)

    def test_devicediscovery(self):
        '''
            Test devicediscoveryserver and devicediscoveryclient. 
            The server registers platform info values, the client connects to the 
            server and fetch the information to print out. 
        '''
        # ensure env is clean
        self.target.run("killall devicediscoveryserver")        
        self.target.run("killall devicediscoveryclient")        
        # start server
        server_cmd = "/opt/iotivity/examples/resource/cpp/devicediscoveryserver > /tmp/svr_output &"
        (status, output) = self.target.run(server_cmd)
        # start client to get info
        client_cmd = "/opt/iotivity/examples/resource/cpp/devicediscoveryclient > /tmp/output &"
        self.target.run(client_cmd)
        time.sleep(2)
        (status, output) = self.target.run('cat /tmp/output')
        # judge if the values are correct
        ret = 0
        if "myPlatformID" in output and "myName" in output and \
           "www.myurl.com" in output and "myModelNumber" in output and \
           "myDateOfManufacture" in output and "platformVersion" in output and \
           "myOS" in output and "myHardwareVersion" in output and \
           "my.Firmware.Version" in output and "www.mysupporturl.com" in output and \
           "mySystemTime" in output:
            pass
        else:
            ret = 1
        self.assertEqual(ret, 0, msg="Error messages: %s" % output)                      
        # kill server and client
        self.target.run("killall devicediscoveryserver")        
        self.target.run("killall devicediscoveryclient")        

    def test_fridge(self):
        '''
            Test fridgeserver and fridgeclient. 
            The server registers resource with 2 doors and 1 light, client connects to the 
            server and fetch the information to print out. 
        '''
        # ensure env is clean
        self.target.run("killall fridgeserver")        
        self.target.run("killall fridgeclient")        
        # start server
        server_cmd = "/opt/iotivity/examples/resource/cpp/fridgeserver > /tmp/svr_output &"
        (status, output) = self.target.run(server_cmd)
        time.sleep(1)
        # start client to get info
        client_cmd = "/opt/iotivity/examples/resource/cpp/fridgeclient > /tmp/output &"
        self.target.run(client_cmd)
        time.sleep(5)
        (status, output) = self.target.run('cat /tmp/output')
        # judge if the values are correct
        ret = 0
        if "Name of device: Intel Powered 2 door, 1 light refrigerator" in output and \
           "Get ID is 1 and resource URI is /light" in output and \
           "Get ID is 2 and resource URI is /door/left" in output and \
           "Get ID is 3 and resource URI is /door/right" in output and \
           "Get ID is 4 and resource URI is /door/random" in output and \
           "Delete ID is 0 and resource URI is /device" in output:
            pass
        else:
            ret = 1
        self.assertEqual(ret, 0, msg="Error messages: %s" % output)                      
        # kill server and client
        self.target.run("killall fridgeserver")        
        self.target.run("killall fridgeclient")        

    def test_garage(self):
        '''
            Test garageserver and garageclient. 
            While server and client communication, remove one attribute Name from 
            OCRepresentation. Then the attribute number of OCRepresentation should 
            reduce 1. 
        '''
        # ensure env is clean
        self.target.run("killall garageserver")        
        self.target.run("killall garageclient")        
        # start server
        server_cmd = "/opt/iotivity/examples/resource/cpp/garageserver > /tmp/svr_output &"
        (status, output) = self.target.run(server_cmd)
        time.sleep(1)
        # start client to get info
        client_cmd = "/opt/iotivity/examples/resource/cpp/garageclient > /tmp/output &"
        self.target.run(client_cmd)
        time.sleep(5)
        (status, output) = self.target.run('cat /tmp/output')
        # judge if the values are correct
        ret = 0
        if "GET request was successful" in output and \
           "attribute: name, was removed successfully from rep2." in output and \
           "Number of attributes in rep2: 6" in output and \
           "PUT request was successful" in output:
            pass
        else:
            ret = 1
        self.assertEqual(ret, 0, msg="Error messages: %s" % output)                      
        # kill server and client
        self.target.run("killall garageserver")        
        self.target.run("killall garageclient")        

    def test_group(self):
        '''
            groupclient has 4 main operations. Only option1 is doable.
            In option (user inputs 1), it will set ActionSet value of rep. This case
            is to check if the set operation is done. 
        '''
        # ensure env is clean
        self.target.run("killall groupserver")        
        self.target.run("killall groupclient")        
        # start server
        server_cmd = "/opt/iotivity/examples/resource/cpp/groupserver > /tmp/svr_output &"
        (status, output) = self.target.run(server_cmd)
        time.sleep(1)
        # start client to get info, here needs user input. So use expect
        exp_cmd = os.path.join(os.path.dirname(__file__), "files/group_client.exp")
        status, output = shell_cmd_timeout("expect %s %s" % (exp_cmd, self.target.ip), timeout=200)
        self.assertEqual(status, 2, msg="expect excution fail")
        # kill server and client
        self.target.run("killall groupserver")        
        self.target.run("killall groupclient")        

    def test_presence_unicast(self):
        '''
            Presence test is complex. It contains 6 sub-tests. 
            Main goal (client) is to observe server resource presence status (presence/stop).
            Every change will trigger a Received presence notification on client side. 
            To each client observation mode:
            -t 1 Unicast                    --- it will receive 7 notifications
            -t 2 Unicast with one filter    --- it will receive 5 notifications
            -t 3 Unicast with two filters   --- it will receive 6 notifications
            -t 4 Multicast                  --- it will receive 7 notifications
            -t 5 Multicast with one filter  --- it will receive 5 notifications
            -t 6 Multicast with two filters --- it will receive 6 notifications
        '''
        number = self.presence_check(1)
        self.assertEqual(number, 7, msg="type 1 should have 7 notifications")

    def test_presence_unicast_one_filter(self):
        ''' See instruction in test_presence_unicast. '''
        number = self.presence_check(2)
        self.assertEqual(number, 5, msg="type 2 should have 5 notifications")

    def test_presence_unicast_two_filters(self):
        ''' See instruction in test_presence_unicast. '''
        number = self.presence_check(3)
        self.assertEqual(number, 6, msg="type 3 should have 6 notifications")

    def test_presence_multicast(self):
        ''' See instruction in test_presence_unicast. '''
        number = self.presence_check(4)
        self.assertEqual(number, 7, msg="type 4 should have 7 notifications")

    def test_presence_multicast_one_filter(self):
        ''' See instruction in test_presence_unicast. '''
        number = self.presence_check(5)
        self.assertEqual(number, 5, msg="type 5 should have 5 notifications")

    def test_presence_multicast_two_filters(self):
        ''' See instruction in test_presence_unicast. '''
        number = self.presence_check(6)
        self.assertEqual(number, 6, msg="type 6 should have 6 notifications")
 
    def test_room_default_collection(self):
        ''' 
            When number is 1 and request is put, light and fan give response individually.
            So, there is no 'In Server CPP entity handler' output. Each respone is given by
            light or fan. 
        '''
        # ensure env is clean
        self.target.run("killall roomserver")        
        self.target.run("killall roomclient")        
        # start server
        server_cmd = "/opt/iotivity/examples/resource/cpp/roomserver 1 > /tmp/svr_output &"
        (status, output) = self.target.run(server_cmd)
        time.sleep(1)
        # start client to get info
        client_cmd = "/opt/iotivity/examples/resource/cpp/roomclient > /tmp/output &"
        self.target.run(client_cmd)
        time.sleep(3)
        (status, output) = self.target.run("cat /tmp/svr_output | grep 'In Server CPP entity handler' -c")
        self.assertEqual(string.atoi(output), 0, msg="CPP entity handler is: %s" % output)                      
        # kill server and client
        self.target.run("killall roomserver")        
        self.target.run("killall roomclient")        

    def test_room_application_collection(self):
        ''' 
            When number is 2 and request is put, room entity handler give light and fan 
            response. So, there are 3 responses output: In Server CPP entity handler.
            In the middle one, it will handle light and fan. 
        '''
        # ensure env is clean
        self.target.run("killall roomserver")        
        self.target.run("killall roomclient")        
        # start server
        server_cmd = "/opt/iotivity/examples/resource/cpp/roomserver 2 > /tmp/svr_output &"
        (status, output) = self.target.run(server_cmd)
        time.sleep(1)
        # start client to get info
        client_cmd = "/opt/iotivity/examples/resource/cpp/roomclient > /tmp/output &"
        self.target.run(client_cmd)
        time.sleep(3)
        (status, output) = self.target.run("cat /tmp/svr_output | grep 'In Server CPP entity handler' -c")
        self.assertEqual(string.atoi(output), 3, msg="CPP entity handler is: %s" % output)                      
        # kill server and client
        self.target.run("killall roomserver")        
        self.target.run("killall roomclient")        

    def test_simple(self):
        '''
            Test simpleserver and simpleclient. 
            After finding resource, simpleclient will do: GET, PUT, POST, Observer sequencely. 
        '''
        # ensure env is clean
        self.target.run("killall simpleserver")        
        self.target.run("killall simpleclient")        
        # start server
        server_cmd = "/opt/iotivity/examples/resource/cpp/simpleserver > /tmp/svr_output &"
        (status, output) = self.target.run(server_cmd)
        time.sleep(1)
        # start client to get info
        client_cmd = "/opt/iotivity/examples/resource/cpp/simpleclient > /tmp/output &"
        self.target.run(client_cmd)
        print "\npatient... simpleclient needs long time for its observation"
        time.sleep(70)
        (status, output) = self.target.run('cat /tmp/output')
        # judge if the values are correct
        ret = 0
        if "DISCOVERED Resource" in output and \
           "GET request was successful" in output and \
           "PUT request was successful" in output and \
           "POST request was successful" in output and \
           "Observe is used." in output and \
           "SequenceNumber: 14" in output:
            pass
        else:
            ret = 1
        self.assertEqual(ret, 0, msg="Error messages: %s" % output)                      
        # kill server and client
        self.target.run("killall simpleserver")        
        self.target.run("killall simpleclient")        

    def test_simpleHQ(self):
        '''
            Test simpleserverHQ and simpleclientHQ. 
            Compared to simpleserver, simpleserverHQ removes SlowResponse, and give
            sendResponse (when PUT) / sendPostResponse (when POST). Basically, they
            are the same.  
        '''
        # ensure env is clean
        self.target.run("killall simpleserverHQ")        
        self.target.run("killall simpleclientHQ")        
        # start server
        server_cmd = "/opt/iotivity/examples/resource/cpp/simpleserverHQ > /tmp/svr_output &"
        (status, output) = self.target.run(server_cmd)
        time.sleep(1)
        # start client to get info
        client_cmd = "/opt/iotivity/examples/resource/cpp/simpleclientHQ > /tmp/output &"
        self.target.run(client_cmd)
        print "\npatient... simpleclientHQ needs long time for its observation"
        time.sleep(70)
        (status, output) = self.target.run('cat /tmp/output')
        # judge if the values are correct
        ret = 0
        if "DISCOVERED Resource" in output and \
           "GET request was successful" in output and \
           "PUT request was successful" in output and \
           "POST request was successful" in output and \
           "Observe is used." in output and \
           "SequenceNumber: 14" in output:
            pass
        else:
            ret = 1
        self.assertEqual(ret, 0, msg="Error messages: %s" % output)                      
        # kill server and client
        self.target.run("killall simpleserverHQ")        
        self.target.run("killall simpleclientHQ")        

    def test_simpleclientserver(self):
        ''' Test simpleclientserver. It foos a server, and start client to do GET/PUT. ''' 
        # ensure env is clean
        self.target.run("killall simpleclientserver")        
        # start test
        client_cmd = "/opt/iotivity/examples/resource/cpp/simpleclientserver > /tmp/output &"
        self.target.run(client_cmd)
        time.sleep(10)
        (status, output) = self.target.run('cat /tmp/output')
        # judge if the values are correct
        ret = 0
        if "Found Resource" in output and \
           "Successful Get" in output and \
           "Successful Put" in output and \
           "barCount: 211" in output:
            pass
        else:
            ret = 1
        self.assertEqual(ret, 0, msg="Error messages: %s" % output)                      
        # kill test
        self.target.run("killall simpleclientserver")        

    def test_threadingsample(self):
        ''' 
            Test threadingsample. In its main(), a foo1 server registered. Then, it opens
            three threads:
             1> second server foo2
             2> clinet1 to detect foo1
             3> client2 to detect foo2, and does GET/PUT further
        ''' 
        # ensure env is clean
        self.target.run("killall threadingsample")        
        # start test
        client_cmd = "/opt/iotivity/examples/resource/cpp/threadingsample > /tmp/output &"
        self.target.run(client_cmd)
        print "\n patient, threadingsample needs some time to open 3 threads"
        time.sleep(20)
        (status, output) = self.target.run('cat /tmp/output')
        # judge if the values are correct
        ret = 0
        if "URI:  /q/foo1" in output and \
           "URI:  /q/foo2" in output and \
           "Successful Get." in output and \
           "Successful Put." in output:
            pass
        else:
            ret = 1
        self.assertEqual(ret, 0, msg="Error messages: %s" % output)                      
        # kill test
        self.target.run("killall threadingsample")        
