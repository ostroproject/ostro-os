# -*- coding: utf8 -*-


"""
@file apprt_python_runtime.py
"""

##
# @addtogroup app_runtime app_runtime
# @brief This is app_runtime component
# @{
# @addtogroup apprt_python_runtime apprt_python_runtime
# @brief This is apprt_python_runtime module
# @{
##

import os
import time

from oeqa.oetest import oeRuntimeTest
from oeqa.utils.decorators import tag


@tag(TestType = 'Functional Positive', FeatureID = 'IOTOS-707')
class PythonRuntimeTest(oeRuntimeTest):
    '''
    This test suite tests whether some basic and key Python modules work well.
    Notice:
        Python upstream tests have been already present in an Ostro OS image.
        The path generally be: /usr/lib/python2.7/test
    @class PythonRuntimeTest
    '''

    python_modules = {
        'os': 'test_os.py',
        'sys': 'test_sys.py',
        'string': 'test_string.py',
        'time': 'test_time.py',
        're': 'test_re.py',
        'shutil': 'test_shutil.py',
        'inspect': 'test_inspect.py',
        'subprocess': 'test_subprocess.py',
        'unittest': 'test_unittest.py',
        'logging': 'test_logging.py',
        'ConfigParser': 'test_cfgparser.py',
        'OptionParser': 'test_optparse.py',
        'csv': 'test_csv.py',
        'StringIO': 'test_StringIO.py',
        'json': 'test_json.py',
        'traceback': 'test_traceback.py'
    }
    test_mod_log = {}
    results_python_runtime = 'results-python-runtime.log'

    @classmethod
    def setUpClass(cls):
        '''
        Clean the workspace before run all the test cases.
        :return:
        @fn setUpClass
        @param cls
        @return
        '''
        if os.path.exists(cls.results_python_runtime):
            os.remove(cls.results_python_runtime)

    @tag(CasesNumber=1364)
    def test_python_runtime(self):
        '''
        Test the Python key standard modules.
        :return:
        @fn test_python_runtime
        @param self
        @return
        '''
        for mod_name, test_mode_file in self.python_modules.items():
            (status, output) = self.target.run(
                'cd /usr/lib/python2.7/test;python %s' % test_mode_file
            )
            self.test_mod_log[mod_name] = output.strip().splitlines()


    @classmethod
    def tearDownClass(cls):
        '''
        Generate the final result output with specified format.
        :return:
        @fn tearDownClass
        @param cls
        @return
        '''
        parse_all_tc(cls.test_mod_log, cls.results_python_runtime)



def line_contains_result(line):
    '''
    Check whether a line contains the results of 'ok', 'FAIL', 'skipped', 'ERROR'
    :param line: A list of one line in the test case log files
    :return: True if the list line contains any test cases running information.
    @fn line_contains_result
    @return
    '''

    return ('ok' in line) or \
           ('FAIL' in line) or \
           ('skipped' in line) or \
           ('ERROR' in line)


def write_tc_name(tc_result, tc, mod_name):
    '''
    Get the test case result of tc_result list and append 'mod_name: tc_name'
    to tc list. The tc_name should be the first element of tc_result.
    :param tc_result:A list of one line in the test case log file.
    :param tc:A list of two elements: [test case name, result]
    :param mod_name:The module name of a test case
    :return:
    @fn write_tc_name
    @return
    '''
    if tc_result:
        tc_name = tc_result[0]
        tc_detailed_name = tc_result[1].strip('()').split('.')[-1]
        tc.append('%s.%s.%s' % (mod_name, tc_detailed_name, tc_name))


def write_tc_result(tc_result, tc):
    '''
    Get the test case result of tc_result list and append it to tc list.
    :param tc_result: A list of one line in the test case log file.
    :param tc: A list of two elements: [test case name, result]
    :return:
    @fn write_tc_result
    @return
    '''
    if 'ok' in tc_result or 'OK' in tc_result:
        tc.append('PASSED')
    elif 'FAIL' in tc_result or 'fail' in tc_result:
        tc.append('FAILED')
    elif 'ERROR' in tc_result or 'error' in tc_result:
        tc.append('ERROR')
    else:
        tc.append(None)


def parse_all_tc(mod_log, result_file):
    '''
    Read all the test cases results. It supports both regular
    and unregular format.
    :param mod_log: The mod:log dictionary
    :param result_file: The final python runtime test case report file.
    :return:
    @fn parse_all_tc
    @return
    '''
    tc_results = []

    for mod, lines in mod_log.items():
        for line_no, line in enumerate(lines):
            tc = []
            if line.startswith('test'):
                tc_result = line.strip().split()

                if ('...' in tc_result) :
                    if line_contains_result(tc_result):
                        write_tc_name(tc_result, tc, mod)
                        write_tc_result(tc_result, tc)

                    else:
                        if line_no < len(lines) - 1:
                            next_tc_result = lines[line_no + 1].strip().split()
                            write_tc_name(tc_result, tc, mod)
                            write_tc_result(next_tc_result, tc)

                elif line_no < len(lines) - 1 and \
                    '...' in lines[line_no + 1] and \
                    (not lines[line_no + 1].startswith('test')):
                    tc_result = line.strip().split()
                    next_tc_result = lines[line_no + 1].strip().split()

                    write_tc_name(tc_result, tc, mod)
                    write_tc_result(next_tc_result, tc)

            elif line_no < len(lines) - 1 and \
                 '...' in lines[line_no + 1] and \
                 (not lines[line_no + 1].startswith('test')):
                tc_result = line.strip().split()
                next_tc_result = lines[line_no + 1].strip().split()

                write_tc_name(tc_result, tc, mod)
                write_tc_result(next_tc_result, tc)

            if None not in tc and tc != []:
                tc_results.append(tc)

    with open(result_file, 'w') as results_f:
        for t in tc_results:
            if None not in t and t != []:
                results_f.write('%s  - runtest.py - RESULTS - Testcase %s: %s\n' %
                        (time.strftime('%H:%M:%S'), t[0], t[1])
                                )

##
# @}
# @}
##

