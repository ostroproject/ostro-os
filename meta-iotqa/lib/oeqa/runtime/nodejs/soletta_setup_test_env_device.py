import os
import sys
import shutil
import json

from get_source import get_test_module_repo

CONST_PATH = os.path.dirname(os.path.realpath(__file__))

def copy_test_files(self, binding):
    '''
    Copy necessary all files related to testing to target device.
    @fn copy_tests_files
    @param self
    '''
    self.local_repo_path = '/tmp/soletta'
    self.repo_test_dir = os.path.join(CONST_PATH, 'files')
    self.target_path = '/usr/lib/node_modules/soletta/soletta-tests/bindings/nodejs/'
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

    os.system("rm -rf soletta-tests/bindings/nodejs/tests/tests/*")

    if binding != "platformService":
        binding_file_list = []
        if binding == "gpio":
            binding_file_list = ["GPIO.js"]
        elif binding == "spi":
            binding_file_list = ["SPI.js"]
        elif binding == "uart":
            binding_file_list = ["UART.js"]
        elif binding == "i2c":
            binding_file_list = ["I2C.js"]
        elif binding == "pwm":
            binding_file_list = ["PWM.js"]
        for test_file in binding_file_list:
            os.system('cp soletta/%s soletta-tests/bindings/nodejs/tests/tests' % test_file)

    compact_cmd = 'tar -cf soletta-tests.tar soletta-tests'
    os.system(compact_cmd)
    cpstatus = self.target.copy_to(
        os.path.join(
            self.repo_test_dir,
            'soletta-tests.tar'
            ),
		"/usr/lib/node_modules/soletta/"
        )
    if cpstatus[0] != 0:
        sys.stderr.write(
            '\nFail to copy soletta-tests to the target device'
            )
        sys.exit(1)

    self.target.run('cd /usr/lib/node_modules/soletta; \
        tar -xf soletta-tests.tar')

    cpstatus1 = self.target.copy_to(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'soletta_upstream_parser_log.py'),
        self.target_path
        )
    if cpstatus1[0] != 0:
        sys.stderr.write(
            '\nFail to copy soletta_upstream_parser_log.py \
            to the target device'
            )
        sys.exit(1)

    if binding == "platformService":
        cpstatus2 = self.target.copy_to(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                'update_suite_js.py'),
            self.target_path
            )
        if cpstatus2[0] != 0:
            sys.stderr.write(
                '\nFail to copy update_suite_js.py to the target device'
                )

def format_results(self, json_path):
    with open(json_path) as data_file:
        data = json.load(data_file)
    res_list = data["output"]
    for i in range(len(res_list)):
        item = res_list[i]["test"]
        caseinfo = res_list[i]["results"]
        for j in range(len(caseinfo)):
            new_item = item.replace(' ', '_')
            #print "@@@@", "".join([new_item, (str(j) + "1")])
            #print "####", "".join(["_", (j + "1")]) 
            case_id = ''.join(new_item, "_", (str(j) + "1"))
            print "debug", case_id
            if "FAIL" == caseinfo[j]["result"]:
                self.addSuccess(case_id)
            else:
                self.addFailure(case_id)
