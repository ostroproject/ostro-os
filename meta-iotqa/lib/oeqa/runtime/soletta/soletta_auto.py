"""
@file soletta_auto.py
"""

##
# @addtogroup soletta
# @brief This is soletta component
# @{
# @addtogroup soletta_auto
# @brief This is soletta_auto module
# @{
##

import os
import re, sys
import time
import subprocess
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import shell_cmd_timeout
from oeqa.utils.helper import get_files_dir
from oeqa.utils.decorators import *
from oeqa.utils.case_interface import *

@tag(TestType="EFT")
@tag(FeatureID="IOTOS-1467")
@tag(CasesNumber=198)
class SolettaUpstreamTestCase(TestCaseInterface):
    """
    @class SolettaUpstreamTestCase
    This is instance of interface "TestCaseInterface" to run soletta upstream test cases
    """
    def setUp(self):
        '''
        @fn setUp
        @param self
        @return
        '''
        self.fbp_test_path = "/usr/lib/soletta/ptest"
        self.fbp_test_log = "soletta-fbp-test.log"
        self.fbp_fake_case = "Soletta_FBP_upstream_tests"
    def process_log_and_gen_resutls(self, fbpLog):
        if not os.path.isfile(fbpLog):
            print(fbpLog)
            self.addFailure(self.fbp_fake_case)
        else:
            print("parse log: " + fbpLog)
            try: 
                filelog = open(fbpLog, 'r')
                for aline in filelog.readlines():
                    print(aline)
                    aline = aline.strip('\n')
                    if re.match(r'^PASS:', aline):
                        self.addSuccess(aline.split(':')[1])
                    elif re.match(r'^FAIL:', aline):
                        self.addFailure(aline.split(':')[1])
                    elif re.match(r'^SKIP:', aline):
                        self.addSkip(aline.split(':')[1])
                    else:
                        continue
            finally: 
                filelog.close()
    def test_soletta_upstream(self):
        '''
        This is for running soletta upstream case in batch
        This test case will not be in final test result
        @fn test_soletta_upstream
        @param self
        @return
        '''
        # check soletta upstream case (ptest) integration
        # TODO: a) soletta integration
        # b) soletta ptest integration
        (status, output) = self.target.run('ls %s' % self.fbp_test_path)
        if (status != 0):
            self.addSkip(self.fbp_fake_case, stdout = "No Soletta fbp test case integration")
        else:
            # run soletta upstream test case
            (status, output) = self.target.run('cd %s; ./run-fbp-tests --log DEBUG --runner /usr/bin/sol-fbp-runner > ./soletta-fbp-test.log 2>&1' % self.fbp_test_path)
            Log = self.fbp_test_path + '/' + self.fbp_test_log
            host_tmp_path = '/tmp'
            self.target.copy_from(Log, host_tmp_path)
            testLog = host_tmp_path + '/' + self.fbp_test_log
            self.process_log_and_gen_resutls(testLog)

##
# @}
# @}
##

