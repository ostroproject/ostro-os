#[PROTEXCAT]
#\License: ALL RIGHTS RESERVED
#\Author: Wang, Jing <jing.j.wang@intel.com>

'''package management test module'''
import os
from oeqa.oetest import oeRuntimeTest

class SmartTest(oeRuntimeTest):
    '''base smarttest'''
    def smart(self, command, expected=0):
        '''smart command'''
        command = 'smart %s' % command
        status, output = self.target.run(command, 1500)
        message = os.linesep.join([command, output])
        self.assertEqual(status, expected, message)
        self.assertFalse("Cannot allocate memory" in output, message)
        return output

class SmartBasicTest(SmartTest):
    '''Basic smart test set'''
    def test_smart_info(self):
        '''test smart info'''
        self.smart('info python-smartpm')

    def test_smart_query(self):
        '''test smart query'''
        self.smart('query python-smartpm')

    def test_smart_search(self):
        '''test smart search'''
        self.smart('search python-smartpm')

    def test_smart_stats(self):
        '''test smart stats'''
        self.smart('stats')
