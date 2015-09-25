'''Verify memory occupied by sensor FW meet M2 target: ~2M'''
import os
from oeqa.oetest import oeRuntimeTest

class TestMemoryUsed(oeRuntimeTest):
    '''Verify memory occupied by sensor FW meet M2 target: ~2M'''
    def testMemoryUsedClean(self):
        '''Verify memory occupied by sensor FW should be less than 2M within clean environment'''
        mkdir_path = "mkdir -p /opt/sensor-test/apps"
        (status, output) = self.target.run(mkdir_path)
        (status, output) = self.target.copy_to(os.path.join(
                    os.path.dirname(__file__), "memuse"), \
"/opt/sensor-test/apps/")
        add_permission_cmd = "chmod 777 /opt/sensor-test/apps/memuse"
        (status, output) = self.target.run(add_permission_cmd)
        client_cmd = "/opt/sensor-test/apps/memuse |grep sensord | awk 'NR==1{print $1}'"
        (status, output) = self.target.run(client_cmd)
        print output
        mem_used = int(filter(str.isdigit, output))     
        print mem_used
        assert mem_used < 2048, 'Memory occupied by sensor FW is larger than M2 target'

    def testMemoryUsedWorking(self):
        '''Verify memory occupied by sensor FW should be less than 2.1M after it works a while'''
        mkdir_path = "mkdir -p /opt/sensor-test/apps"
        (status, output) = self.target.run(mkdir_path)
        (status, output) = self.target.copy_to(os.path.join(
                    os.path.dirname(__file__), "memuse"), \
"/opt/sensor-test/apps/")
        add_permission_cmd = "chmod 777 /opt/sensor-test/apps/memuse"
        (status, output) = self.target.run(add_permission_cmd)
        client_cmd = "/opt/sensor-test/apps/memuse |grep sensord | awk 'NR==1{print $1}'"
        (status, output) = self.target.run(client_cmd)
        print output
        mem_used = int(filter(str.isdigit, output))
        print mem_used
        assert mem_used < 2248, 'Memory leak happens after sensor FW works a while'
