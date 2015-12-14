#[PROTEXCAT]
#\License: ALL RIGHTS RESERVED
#\Author: Wang, Jing <jing.j.wang@intel.com>

'''base os test module
@file baseos.py
'''

##
# @addtogroup sanity sanity
# @brief This is sanity component
# @{
# @addtogroup baseos baseos
# @brief This is baseos module
# @{
##

from oeqa.oetest import oeRuntimeTest

class BaseOsTest(oeRuntimeTest):
    '''Base os health check
    @class BaseOsTest
    '''
    def test_baseos_dmesg(self):
        '''check dmesg command
        @fn test_baseos_dmesg
        @param self
        @return
        '''
        (status, output) = self.target.run('dmesg')
        ##
        # TESTPOINT: #1, test_baseos_dmesg
        #
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

    def test_baseos_lsmod(self):
        '''check lsmod command
        @fn test_baseos_lsmod
        @param self
        @return
        '''
        (status, output) = self.target.run('lsmod')
        ##
        # TESTPOINT: #1, test_baseos_lsmod
        #
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

    def test_baseos_ps(self):
        '''check ps command
        @fn test_baseos_ps
        @param self
        @return
        '''
        (status, output) = self.target.run('ps')
        ##
        # TESTPOINT: #1, test_baseos_ps
        #
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

    def test_baseos_df(self):
        '''check df command
        @fn test_baseos_df
        @param self
        @return
        '''
        (status, output) = self.target.run('df')
        ##
        # TESTPOINT: #1, test_baseos_df
        #
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

    def test_baseos_systemd_process(self):
        '''check systemd process
        @fn test_baseos_systemd_process
        @param self
        @return
        '''
        (status, output) = self.target.run("ls -l /proc/1/exe | grep 'systemd'")
        ##
        # TESTPOINT: #1, test_baseos_systemd_process
        #
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

    def test_baseos_sensord_process(self):
        '''check sensord process
        @fn test_baseos_sensord_process
        @param self
        @return
        '''
        (status, output) = self.target.run("ps | grep -v grep | grep sensord")
        ##
        # TESTPOINT: #1, test_baseos_sensord_process
        #
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

##
# @}
# @}
##

