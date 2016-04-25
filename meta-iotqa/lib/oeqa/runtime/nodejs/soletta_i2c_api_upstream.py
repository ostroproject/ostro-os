import os
import sys
import shutil
import subprocess


from oeqa.oetest import oeRuntimeTest
from oeqa.utils.decorators import tag
from oeqa.utils.case_interface import *
from get_source import get_test_module_repo
from soletta_setup_test_env_device import *


CONST_PATH = os.path.dirname(os.path.realpath(__file__))

@tag(TestType='FVT', FeatureID='IOTOS-1155')
class solettai2cApiTest(TestCaseInterface):
    '''
    @class solettai2cApiTest
    Update suite.js for testing
    '''
    def setUp(self):
        '''
        Copy all files related to testing to device
        @fn setup
        @param self
        '''
        # Download the repository of soletta
        sys.stdout.write('\nDownloading the repository of soletta...')
        sys.stdout.flush()
        soletta_url = 'https://github.com/solettaproject/soletta.git'
        get_test_module_repo(soletta_url, 'soletta')

        sys.stdout.write('\nCopying necessary files to target device...')
        sys.stdout.flush()

        # Copy all files related to testing to device
        binding = "i2c"
        copy_test_files(self, "i2c")
        sys.stdout.write(
            '\nCopy all files related to testing to target device done!'
            )
        sys.stdout.flush()

        # Update suite.js
        self.target.run('python %s/update_suite_js.py' %
                self.target_path
            )


    @tag(CasesNumber=1)
    def test_sol_i2c_api(self):
        '''
        Execute the soletta upstream test cases.
        @fn test_sol_platform_service_api
        @param self
        '''
        sys.stdout.write(
            '\nExecuting soletta i2c upstream test cases...'
            )
        sys.stdout.flush()
        run_grunt_cmd = ''.join([
            'cd ',
            self.target_path,
            '; node tests/suite.js'
            ])
        (status, output) = self.target.run(run_grunt_cmd)
        sys.stdout.write('\r' + ' ' * 78 + '\r')
        #sys.stdout.write(''.join(['\n', output]))
        sys.stdout.flush()
        result_log = self.target_path + "tests/results.json"
        local_path = "/tmp"
        json_path = local_path + "/results.json"
        self.target.copy_from(result_log, local_path)
        format_results(self, json_path)


    def tearDown(self):
        '''
        Clean work: remove all the files downloaded on host and
        copied to the target device during the test.
        @fn tearDown
        @param self
        '''
        sys.stdout.write("\nClean test files on host")
        sys.stdout.flush()
        os.system('rm -rf %s/soletta-tests*' % self.repo_test_dir)
        sys.stdout.write("\nClean test files on device")
        sys.stdout.flush()
        self.target.run('rm -rf /usr/lib/node_modules/soletta/soletta-tests*')
        sys.stdout.write('\nClean all files related to testing done!!\n')
        sys.stdout.flush()


##
# @}
# @}
##

