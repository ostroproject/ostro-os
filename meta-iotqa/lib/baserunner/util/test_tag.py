'''
Created on Mar 30, 2016

@author: iot
'''
import unittest
from tag import *
class MyDict(dict):
    def __getitem__(self, *args, **kwargs):
        ret = super(MyDict, self).__getitem__(*args, **kwargs)
        print args[0], ret
        return ret
class MyDict2(dict):
    def __getitem__(self, key):
        ret = super(MyDict2, self).__getitem__(key)
        print key, ret
        return ret
#print "test" in MyDict2(test=1)
class MyDict3(dict):
    def __init__(self, testcase, *args, **kwargs):
        super(MyDict3, self).__init__(*args, **kwargs)
        self.testcase = testcase
    def __getitem__(self, key):
        #ret = super(MyDict3, self).__getitem__(key)
        if hastag(self.testcase, key):
            ret = gettag(self.testcase, key)
            return ret
        return super(MyDict3, self).__getitem__(key)

def mygetvar(**kwargs):
    """if a variable not exist, find it in testcase"""
    class VarDict(dict):
        """wrapper of var dict"""
        def __getitem__(self, key):
            ret = kwargs[key]
            print key,ret
            return ret
    return VarDict()

def getvar(obj):
    """if a variable not exist, find it in testcase"""
    class VarDict(dict):
        """wrapper of var dict"""
        def __getitem__(self, key):
            ret = gettag(obj, key)
            print key, ret
            return ret
    return VarDict()

class MyTest(unittest.TestCase):
    #@tag("BAT", a="a", b="a b c")
    def test_print(self):
        print "ok"

if __name__ == '__main__':
    exp = "BAT == True"
    t = MyTest("test_print")
    #print checktags(t, "'a' in [x for x in b.split()]")
    print 1
    print checktags(t, exp)
#     print 2
#     print eval(exp, getvar(t))
#     print 3
#     print eval(exp, MyDict(BAT=True))
#     print 4
#     print eval(exp, MyDict2(BAT=True))
#     print 5
#     print eval(exp, MyDict3(t))
#     print 6
#     print eval(exp, mygetvar(BAT=True))


