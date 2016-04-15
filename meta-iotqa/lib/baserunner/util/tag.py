#!/usr/bin/env python
# Copyright (C) 2013 Intel Corporation
#
# Released under the MIT license (see COPYING.MIT)

# Tag filter module used by testrunner
# This provides tag based filtering function for test case set.

"""Tag Filter Module"""
import unittest

TAG_PREFIX = "tag__"
def tag(*args, **kwargs):
    """tag decorator that adds attributes to classes or functions"""
    def wrap_obj(obj):
        """wrap function"""
        for name in args:
            setattr(obj, TAG_PREFIX + name, True)
        for name, value in kwargs.iteritems():
            setattr(obj, TAG_PREFIX + name, value)
        return obj
    return wrap_obj

def hastag(obj, key):
    """check if obj has a tag"""
    key = TAG_PREFIX + key
    if not isinstance(obj, unittest.TestCase):
        return hasattr(obj, key)
    tc_method = getattr(obj, obj._testMethodName)
    return hasattr(tc_method, key) or hasattr(obj, key)

def gettag(obj, key, default=None):
    """get a tag value from obj"""
    key = TAG_PREFIX + key
    if not isinstance(obj, unittest.TestCase):
        return getattr(obj, key, default)
    tc_method = getattr(obj, obj._testMethodName)
    return getattr(tc_method, key, getattr(obj, key, default))

def getvar(obj):
    """if a variable not exist, find it in testcase"""
    class VarDict(dict):
        """wrapper of var dict"""
        def __getitem__(self, key):
            # expression may be set a var in this dict
            if key in self:
                return super(VarDict, self).__getitem__(key)
            if hastag(obj, key):
                return gettag(obj, key)
            # maybe some build-in object
            try:
                return eval(key, {}, {})
            except:
                return False

    return VarDict()

def checktags(testcase, tagexp):
    """eval tag expression and return the result"""
    return eval(tagexp, None, getvar(testcase))

def filter_tagexp(testsuite, tagexp):
    """filter according to true or flase of tag expression"""
    if not tagexp:
        return testsuite
    caselist = []
    for each in testsuite:
        if not isinstance(each, unittest.BaseTestSuite):
            if checktags(each, tagexp):
                caselist.append(each)
        else:
            caselist.append(filter_tagexp(each, tagexp))
    return testsuite.__class__(caselist)

def _testset(testsuite):
    """iterate tc in testsuite"""
    for each in testsuite:
        if unittest.suite._isnotsuite(each):
            yield each
        else:
            for each2 in _testset(each):
                yield  each2

class TagInformations(object):
    """Get all tags informations of test suite"""
    def __init__(self, tests):
        self.tests = tests

    def _testset(self):
        for each in _testset(self.tests):
            yield each

    def count(self):
        """test cases count"""
        ret = 0
        for test in self._testset():
            ret += test.countTestCases()
        return ret

    def group_by(self, key):
        """group by key, return key/val dict"""
        ret = {}
        for test in self._testset():
            if hastag(test, key):
                ret.setdefault(gettag(test, key), []).append(test)
                continue
            ret.setdefault("others", []).append(test)
        for k in ret:
            ret[k] = self.__class__(ret[k])
        return ret

    def get_sum(self, *args, **kwargs):
        """get summary report"""
        assert len(args) + len(kwargs) == 1
        lst = []
        for test in self._testset():
            if args:
                if hastag(test, args[0]):
                    lst.append(test)
            elif kwargs:
                k, v = kwargs.items()[0]
                if gettag(test, k) == v:
                    lst.append(test)
        return self.__class__(lst)
