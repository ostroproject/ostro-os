import json
import os
import sys

SCRIPT_PATH = os.path.realpath(__file__)
CONST_PATH = os.path.dirname(SCRIPT_PATH)
JSON_PATH = os.path.join(CONST_PATH, "tests/results.json")

def format_results(json_path):
    with open(json_path) as data_file:
        data = json.load(data_file)
    res_list = data["output"]
    for i in range(len(res_list)):
        item = res_list[i]["test"]
        caseinfo = res_list[i]["results"]
        for j in range(len(caseinfo)):
            run_time = caseinfo[j]["runtime"]
            if "FAIL" == caseinfo[j]["result"]:
                result = "FAILED"
            else:
                result = "PASSED"
        case_id = item.replace(' ', '_')
        case_result_info = ''.join([
            run_time,
            ' - runtest.py - RESULTS - Testcase ',
            case_id,
            ': ',
            result,
            '\n'
            ])
        sys.stdout.write(case_result_info)

if __name__ == '__main__':
    format_results(JSON_PATH)
