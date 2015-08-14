#!/usr/bin/env python

import os, sys
from optparse import OptionParser
import unittest
import csv

BASEDIR = os.path.abspath(os.path.dirname(__file__))
TOPDIR = os.path.dirname(BASEDIR)
TITLE = ["EntityType", "CaseID", "Component", "Description",
         "TestType", "Status", "FeatureID", "ExecutionType",
         "PreCondition", "PostCondition",
         "StepNumber", "StepDescription", "ExpectedResult",
         "TestScriptEntry", "TestScriptExpectResult" ]
COLUMN_NUM = len(TITLE)

def parseArgs():
    usage = "usage: %prog [options]"
    parser = OptionParser(usage=usage)
    parser.add_option("-r", "--root-dir", dest="root",
            default = TOPDIR,
            help="root dir of ostro")
    parser.add_option("-m", "--manual", dest="manual",
            default = os.path.join(BASEDIR, "conf", "test", "manual.csv"),
            help="The manual cases csv file.")
    parser.add_option("-o", "--output-file", dest="output",
            default  = "out.csv",
            help="The output file name.")

    return parser.parse_args()

def getCaseList(path, pypath=["oeqa", "runtime"]):
    testslist = []
    if not os.path.exists(os.path.join(path, '__init__.py')):
        print("%s __init__.py missing!"%path)
        return []
    for f in os.listdir(path):
        fullpath = os.path.join(path, f)
        if os.path.isfile(fullpath):
            if f.endswith('.py') and not f.startswith('_'):
                pypath.append(f[:-3])
                m = pypath[:]
                pypath.pop()
                if m not in testslist:
                    testslist.append(m)
        elif os.path.isdir(fullpath):
            pypath.append(f)
            testslist.extend(getCaseList(fullpath, pypath))
            pypath.pop()
    return testslist


def getTagValue(case, key, default=""):
    return getattr(case, key, getattr(case.__class__, key, default))

__opDict = {"EntityType"   : lambda x, y, z: "TestScript",
            "CaseID"       : lambda x, y, z: x.id(),
            "Description"  : lambda x, y, z: x._testMethodDoc if x._testMethodDoc else z,
            }
def getValueFromCase(case, key, default=""):
    return __opDict.get(key, getTagValue)(case, key, default)

def caseIter(testsuite):
    for x in testsuite:
        if not isinstance(x, unittest.BaseTestSuite):
            yield x
        else:
            for y in caseIter(x):
                yield y

def getCasesInfo(pathList):
    entityType = "TestScript"
    rows = []
    defaultValList = [""] * COLUMN_NUM
    casename = ".".join(pathList)
    defaultComponent = pathList[-2] if len(pathList)>3 else "None"
    try:
        testsuite = unittest.TestLoader().loadTestsFromName(casename)
    except:
        print >>sys.stderr, "Import %s Failed"%".".join(pathList)
        return []
    defaultValList[TITLE.index("Component")] = defaultComponent
    defaultValList[TITLE.index("Status")] = "Ready"
    defaultValList[TITLE.index("ExecutionType")] = "Auto"
    for case in caseIter(testsuite):
        print "Testcase:", case.id()
        row = map(getValueFromCase, [case]*COLUMN_NUM, TITLE, defaultValList)
        rows.append(row)
    return rows

def main():
    opt, args = parseArgs()
    sys.path.append(os.path.join(TOPDIR, "bitbake", "lib"))
    sys.path.append(os.path.join(TOPDIR, "meta", "lib"))
    for dir in os.listdir(TOPDIR):
        libPath = os.path.join(TOPDIR, dir, "lib")
        if os.path.exists(libPath) and libPath not in sys.path:
            sys.path.insert(0, libPath)
    from oeqa.oetest import oeTest, loadTests, oeRuntimeTest
    from oeqa.runexported import MyDataDict, FakeTarget, TestContext
    import oeqa.utils
    tc = TestContext()
    setattr(oeTest, "tc", tc)
    d = MyDataDict()
    with open(opt.output, "w") as output, open(opt.manual, "r") as manual:
        outputcsv = csv.writer(output)
        outputcsv.writerow(TITLE)
        for dir in os.listdir(TOPDIR):
            libPath = os.path.join(TOPDIR, dir, "lib")
            oeqaPath = os.path.join(libPath, "oeqa")
            runtimePath = os.path.join(oeqaPath, "runtime")
            if os.path.exists(runtimePath):
                for case in getCaseList(runtimePath):
                    rows = getCasesInfo(case)
                    for row in rows:
                        outputcsv.writerow(row)
        manualcsv = csv.reader(manual)
        manualTitle = []
        mapIndex = [0, 1, 2, 3, 7, 8, 9, 10, 11, 4, 5, 6,  12, 13, 14]
        def convertManualToOut(row):
            ret = []
            for title in TITLE:
                v = ""
                try:
                    i = manualTitle.index(title)
                    v = line[i]
                except ValueError:
                    if title == "ExecutionType" and line[0] == "TestScript":
                        v = "Manual"
                except:
                    raise Exception("Please input a correct manuual csv file")
                ret.append(v)
            return ret
        for line in manualcsv:
            if manualcsv.line_num == 1:
                manualTitle = line
            else:
                row = convertManualToOut(line)
                outputcsv.writerow(row)
    print "Done. Generate csv to:", os.path.abspath(opt.output)
if __name__ == "__main__":
    main()

