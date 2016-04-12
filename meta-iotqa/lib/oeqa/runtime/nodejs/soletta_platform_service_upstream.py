import os
import sys
import shutil
import subprocess


from oeqa.oetest import oeRuntimeTest
from oeqa.utils.decorators import tag
from get_source import get_test_module_repo

CONST_PATH = os.path.dirname(os.path.realpath(__file__))

def copy_test_files(self):
    '''
    Copy necessary all files related to testing to target device.
    @fn copy_tests_files
    @param self
    '''
    self.local_repo_path = '/tmp/soletta'
    self.repo_test_dir = os.path.join(CONST_PATH, 'files')
    self.target_path = '/usr/lib/node_modules/'
    os.chdir(self.repo_test_dir)
    os.mkdir('soletta-tests')
    copy_list = ['bindings/nodejs/', 'node_modules',
                'lowlevel.js', 'index.js', 'package.json']

    for single_file in copy_list:
        single_file_path = os.path.join(self.local_repo_path, single_file)
        if os.path.isfile(single_file_path):
            shutil.copyfile(os.path.join(self.local_repo_path, single_file),
                            os.path.join(self.repo_test_dir, 'soletta-tests',
                            single_file))
        elif os.path.isdir(single_file_path):
            shutil.copytree(os.path.join(self.local_repo_path, single_file),
                            os.path.join(self.repo_test_dir, 'soletta-tests',
                                single_file))

    os.system('cp %s/solettaplatform/getresult.js \
        %s/soletta-tests/bindings/nodejs/tests' %
        (self.repo_test_dir, self.repo_test_dir)
        )
    compact_cmd = 'tar -cf soletta-tests.tar soletta-tests'
    os.system(compact_cmd)
    cpstatus = self.target.copy_to(
        os.path.join(
            self.repo_test_dir,
            'soletta-tests.tar'
            ),
        self.target_path
        )
    if cpstatus[0] != 0:
        sys.stderr.write(
            '\nFail to copy soletta-tests to the target device'
            )
        sys.exit(1)

    self.target.run('cd /usr/lib/node_modules; tar -xf soletta-tests.tar')

    cpstatus1 = self.target.copy_to(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'soletta_platform_service_upstream_parser_log.py'),
        os.path.join(
            self.target_path,
            'soletta-tests/bindings/nodejs/'
            )
        )
    if cpstatus1[0] != 0:
        sys.stderr.write(
            '\nFail to copy soletta_platform_service_upstream_parser_log.py \
            to the target device'
            )
        sys.exit(1)

    cpstatus2 = self.target.copy_to(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'update_setup_suite_js.py'),
        os.path.join(
            self.target_path,
            'soletta-tests/bindings/nodejs'
            )
        )
    if cpstatus2[0] != 0:
        sys.stderr.write(
            '\nFail to copy update_setup_suite_js.py to the target device'
            )
        sys.exit(1)

@tag(TestType='FVT', FeatureID='IOTOS-1157')
class solettaplatformServiceApiTest(oeRuntimeTest):
    '''
    @class solettaplatformServiceApiTest

    Backup for setup.js, suite.js and update it for testing
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
        copy_test_files(self)
        sys.stdout.write(
            '\nCopy all files related to testing to target device done!'
            )
        sys.stdout.flush()

        # Update setup.js and suite.js
        self.target.run('python %s/soletta-tests/bindings/nodejs/update_setup_suite_js.py' %
                self.target_path
            )


    @tag(CasesNumber=1)
    def test_sol_platform_service_api(self):
        '''
        Execute the soletta upstream test cases.
        @fn test_sol_platform_service_api
        @param self
        '''
        sys.stdout.write(
            '\nExecuting iotivity-node upstream test cases...'
            )
        sys.stdout.flush()
        run_grunt_cmd = ''.join([
            'cd ',
            self.target_path,
            'soletta-tests/bindings/nodejs; node tests/suite.js'
            ])
        format_result_cmd = ''.join([
            'python ',
            self.target_path,
            'soletta-tests/bindings/nodejs/soletta_platform_service_upstream_parser_log.py'
            ])
        (status, output) = self.target.run(run_grunt_cmd)
        sys.stdout.write('\r' + ' ' * 78 + '\r')
        sys.stdout.write(''.join(['\n', output]))
        sys.stdout.flush()
        (status, output) = self.target.run(format_result_cmd)
        sys.stdout.write('\r' + ' ' * 78 + '\r')
        sys.stderr.write(''.join(['\n', output, '\n']))
        sys.stdout.flush()

    def tearDown(self):
        '''
        Clean work: remove all the files downloaded on host and
        copied to the target device during the test.
        @fn tearDown
        @param self
        '''
        sys.stdout.write("\nClean test files on host")
        sys.stdout.flush()
        os.system('rm -rf %s/soletta-tests %s/soletta-tests.tar' %
            (self.repo_test_dir, self.repo_test_dir)
            )
        sys.stdout.write("\nClean test files on device")
        sys.stdout.flush()
        self.target.run('rm -rf /usr/lib/node_modules/soletta-tests.tar')
        self.target.run('rm -rf /usr/lib/node_modules/soletta-tests')
        sys.stdout.write('\nClean all files related to testing done!!\n')
        sys.stdout.flush()


##
# @}
# @}
##

