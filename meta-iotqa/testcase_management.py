#!/usr/bin/env python

import os, sys, re
from optparse import OptionParser
import unittest
import csv
import StringIO
import logging

BASEDIR = os.path.abspath(os.path.dirname(__file__))
_IS_EXPORTED_SUITE = os.path.exists(os.path.join(BASEDIR, "testplan"))
TOPDIR =  BASEDIR if _IS_EXPORTED_SUITE else os.path.dirname(BASEDIR)
if _IS_EXPORTED_SUITE:
    def addPaths():
        sys.path.append(os.path.join(TOPDIR, "bitbake", "lib"))
        sys.path.append(os.path.join(TOPDIR, "oeqa"))
else:
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

PLATFORMS_DICT = {"GB-BXBT"    : r"gbbxbt",
                  "Galileo"    : r"galileo", 
                  "MinnowMax"  : r"minnowmax", 
                  "Edison"     : r"edison", 
                  "VirtualBox" : r"virtualbox" }
_PLAN_DIR = os.path.join(BASEDIR, "testplan") if _IS_EXPORTED_SUITE else \
            os.path.join(BASEDIR, "conf", "test")

class CaseInfo(object):
    planPattern = re.compile(r"(?:(?P<platform>[^.]+)\.)?(?P<component>[^.]+).manifest$", re.I)
    casesNumberPattern = re.compile(r"CasesNumber=(\d+)")
    def __init__(self, planPath=_PLAN_DIR, platform=None):
        if isinstance(planPath, list):
            files = planPath
        else:
            files = [os.path.join(planPath, f) for f in os.listdir(planPath)]
        self.platform = platform
        self.planDict = {}
        for filename in files:
            m = self.planPattern.match(os.path.basename(filename))
            if m:
                groupd = m.groupdict()
                logging.info("find manifest file: %s" % filename)
                self.planDict.setdefault(groupd["component"], {})[groupd["platform"]] = filename
        self.manifestContextDict = {}
        self.caseInfoDict={}
        self.getCaseInfo()
    
    def __filesIter__(self):
        for component, v in self.planDict.items():
            if self.platform is not None:
                yield component, self.platform if self.platform in v else None, v.get(self.platform, v[None])
            else:
                for platform, filename in v.items():
                    yield component, platform, filename

    def readManifestFiles(self):
        for component, platform, filename in self.__filesIter__():
            logging.info("reading form %s"%filename)
            self.manifestContextDict[(component, platform, filename)] = []
            with open(filename, "r") as f:
                map(lambda y:self.manifestContextDict[(component, platform, filename)].append(y) if y not in self.manifestContextDict[(component, platform, filename)] else None, 
                    filter(lambda x: not x.startswith('#'),
                                  [n.strip() for n in f.readlines()])
                    )
        return self.manifestContextDict

    def getCaseInfo(self):
        self.readManifestFiles()
        for k in self.__filesIter__():
            tclist = self.manifestContextDict[k]
            #self.caseInfoDict[k[0]] = _getCasesInfo(tclist, k[0])
            self.caseInfoDict.setdefault(k[0], {})[k[1]] = _getCasesInfo(tclist, k[0])

    def __iter__(self):
        for each in self.__filesIter__():
            yield each

    def __getitem__(self, key):
        if isinstance(key, tuple):
            return self.caseInfoDict[key[0]][key[1]]
        return None

    otherIndex = TITLE.index("Other")
    def countCases(self, caseList):
        ret = 0
        for case in caseList:
            otherInfo = case[self.otherIndex]
            if otherInfo:
                m = re.findall(self.casesNumberPattern, otherInfo)
                if m:
                    ret += int(m[0]) - 1
            ret += 1
        return ret

    def getCasesCount(self, platform=None):
        ret = 0
        for name, v in self.caseInfoDict.items():
            caseList = v.get(platform, v.get(None, []))
            ret += self.countCases(caseList)
        return ret

def parseArgs():
    usage = """usage: %prog [options]"""
    parser = OptionParser(usage=usage)
    if not _IS_EXPORTED_SUITE:
        parser.add_option("-c", "--classic", dest="classic",
            help="classic model, scan all test cases.")
        parser.add_option("-r", "--root-dir", dest="root",
            default = TOPDIR,
            help="root dir of ostro")
        parser.add_option("-l", "--layer", dest="layers",
            action="append",
            help="specify layer to export. if layers count is greater than 1: -l [layer1] -l [layer2]..")
#        parser.add_option("-L", "--skip-layer", dest="skip_layers",
#             action="append",
#             help="specify layer don't export. if layers count is greater than 1: -L [layer1] -L [layer2]..")
    parser.add_option("-f", "--file", dest="file",
        help="The manifest file. if manifest files count is greater than 1: -f [file1] -f [file2]..")
    parser.add_option("-p", "--platform", dest="platform",
        help="platform infomation: %s and all, Default is None."%PLATFORMS_DICT.keys())
    parser.add_option("-m", "--manual", dest="manual",
            default = os.path.join(BASEDIR, "testplan", "manual.csv") if _IS_EXPORTED_SUITE \
            else os.path.join(BASEDIR, "conf", "test", "manual.csv"),
            help="The manual cases csv file.")
    parser.add_option("-o", "--output-file", dest="output",
            default  = "out.csv",
            help="The output file name.")
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
def _getCasesInfo(casename, component=None, layer="None"):
    entityType = "TestScript"
    rows = []
    defaultValList = [""] * COLUMN_NUM
    defaultComponent = component
    output = StringIO.StringIO()
    oristdout, oristderr = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = output, output
    loader = unittest.TestLoader()
    caseList = [casename] if isinstance(casename, str) else casename
    testsuite = []
    for case in caseList:
        try:
            s = loader.loadTestsFromName(case) 
            testsuite.append(s) 
        except:
            logging.warn("Import %s Failed"%(case))
    sys.stdout, sys.stderr = oristdout, oristderr
    output.getvalue() and logging.debug(output.getvalue())
    output.close()
    defaultValList[TITLE.index("Component")] = defaultComponent
    defaultValList[TITLE.index("Status")] = "Ready"
    defaultValList[TITLE.index("ExecutionType")] = "Auto"
    for case in caseIter(testsuite):
        logging.info( "Testcase: ", case.id())
        row = map(getValueFromCase, [case]*COLUMN_NUM, TITLE, defaultValList)
        rows.append(row)
    return rows

def getCasesInfo(pathList, component=None, layer="None"):
    casename = ".".join(pathList)
    component = component if component is not None\
                  else pathList[-2] if len(pathList)>3 else layer
    return _getCasesInfo(casename, component, layer)

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
    
    with open(opt.output, "w") as output, open(opt.manual, "r") as manual:
        outputcsv = csv.writer(output)
        if hasattr(opt, "classic") and opt.classic:
            outputcsv.writerow(TITLE)
            dirs = opt.layers if opt.layers and not opt.layers[0].startswith("!") else os.listdir(TOPDIR)
            notdirs = opt.skip_layers if opt.skip_layers else []
            dirs = filter(lambda x: x not in notdirs, dirs)
            
            for dir in dirs:
                libPath = os.path.join(TOPDIR, dir, "lib")
                oeqaPath = os.path.join(libPath, "oeqa")
                runtimePath = os.path.join(oeqaPath, "runtime")
                if os.path.exists(runtimePath):
                    for case in getCaseList(runtimePath):
                        rows = getCasesInfo(case, layer=dir)
                        for row in rows:
                            outputcsv.writerow(row)
        else:
            caseinfos = CaseInfo()
            print "all cases count:", caseinfos.getCasesCount()
            outputcsv.writerow(["all cases count:", caseinfos.getCasesCount()])
            for k, v in PLATFORMS_DICT.items():
                print "%s cases count:"%k, caseinfos.getCasesCount(v)
                outputcsv.writerow(["%s cases count:"%k, caseinfos.getCasesCount(v)])
            for k in caseinfos:
                print k[2], ":", caseinfos.countCases(caseinfos[k])
                outputcsv.writerow([k[2], caseinfos.countCases(caseinfos[k])])
            outputcsv.writerow(TITLE)
            for k in caseinfos:
                rows = caseinfos[k]
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

    