#!/usr/bin/env python

import os, sys
from optparse import OptionParser
import unittest
import csv
import StringIO
import logging

BASEDIR = os.path.abspath(os.path.dirname(__file__))
TOPDIR = os.path.dirname(BASEDIR)
def addPaths():
    sys.path.append(os.path.join(TOPDIR, "bitbake", "lib"))
    sys.path.append(os.path.join(TOPDIR, "meta", "lib"))
    for dir in os.listdir(TOPDIR):
        libPath = os.path.join(TOPDIR, dir, "lib")
        if os.path.exists(libPath) and libPath not in sys.path:
            sys.path.insert(0, libPath)
addPaths()
from oeqa.utils.decorators import gettag, getAllTags

TITLE = ["EntityType", "CaseID", "Component", "Description",
         "TestType", "Status", "FeatureID", "ExecutionType",
         "PreCondition", "PostCondition",
         "StepNumber", "StepDescription", "ExpectedResult",
         "TestScriptEntry", "TestScriptExpectResult", "Other" ]
COLUMN_NUM = len(TITLE)

LOG_LEVEL = logging.WARNING

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
    parser.add_option("-l", "--layer", dest="layers",
            action="append",
            help="specify layer to export. if layers count is greater than 1: -l [layer1] -l [layer2]..")
    parser.add_option("-L", "--skip-layer", dest="skip_layers",
            action="append",
            help="specify layer don't export. if layers count is greater than 1: -L [layer1] -L [layer2]..")
    parser.add_option("-v", "--verbose", dest="verbose",
            action="store_true",
            help="print verbose information")
    return parser.parse_args()

def getCaseList(path, pypath=["oeqa", "runtime"]):
    testslist = []
    if not os.path.exists(os.path.join(path, '__init__.py')):
        logging.warn("Ignore %s due to __init__.py is missing!"%path)
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

__title = TITLE[:]
__title.pop()
def getOtherInfo(case, key, default=""):
    ret = []
    for k, v in getAllTags(case).iteritems():
        if k not in __title:
            ret.append("%s=%r"%(k, v))
    return ", ".join(ret) if ret else default

def getTagValue(case, key, default=""):
    return gettag(case, key, default)

__opDict = {"EntityType"   : lambda x, y, z: "TestScript",
            "CaseID"       : lambda x, y, z: x.id(),
            "Description"  : lambda x, y, z: x._testMethodDoc if x._testMethodDoc else z,
            "Other"        : getOtherInfo
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

def getCasesInfo(pathList, layer="None"):
    entityType = "TestScript"
    rows = []
    defaultValList = [""] * COLUMN_NUM
    casename = ".".join(pathList)
    defaultComponent = pathList[-2] if len(pathList)>3 else layer
    output = StringIO.StringIO()
    oristdout, oristderr = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = output, output
    try:
        testsuite = unittest.TestLoader().loadTestsFromName(casename)
    except:
        logging.warn("Import %s:%s Failed"%(layer, ".".join(pathList)))
        return []
    finally:
        sys.stdout, sys.stderr = oristdout, oristderr
        logging.debug(output.getvalue())
        output.close()
    defaultValList[TITLE.index("Component")] = defaultComponent
    defaultValList[TITLE.index("Status")] = "Ready"
    defaultValList[TITLE.index("ExecutionType")] = "Auto"
    for case in caseIter(testsuite):
        logging.info( "Testcase: ", case.id())
        row = map(getValueFromCase, [case]*COLUMN_NUM, TITLE, defaultValList)
        rows.append(row)
    return rows

def main():
    opt, args = parseArgs()
    if opt.verbose:
        global LOG_LEVEL
        LOG_LEVEL = logging.NOTSET
    logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s: %(message)s")
    from oeqa.oetest import oeTest, loadTests, oeRuntimeTest
    from oeqa.runexported import MyDataDict, FakeTarget, TestContext
    import oeqa.utils
    tc = TestContext()
    setattr(oeTest, "tc", tc)
    d = MyDataDict()
    dirs = opt.layers if opt.layers else os.listdir(TOPDIR)
    notdirs = opt.skip_layers if opt.skip_layers else []
    dirs = filter(lambda x: x not in notdirs, dirs)
    with open(opt.output, "w") as output, open(opt.manual, "r") as manual:
        outputcsv = csv.writer(output)
        outputcsv.writerow(TITLE)
        for dir in dirs:
            libPath = os.path.join(TOPDIR, dir, "lib")
            oeqaPath = os.path.join(libPath, "oeqa")
            runtimePath = os.path.join(oeqaPath, "runtime")
            if os.path.exists(runtimePath):
                for case in getCaseList(runtimePath):
                    rows = getCasesInfo(case, dir)
                    for row in rows:
                        outputcsv.writerow(row)
        manualcsv = csv.reader(manual)
        manualTitle = []
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

