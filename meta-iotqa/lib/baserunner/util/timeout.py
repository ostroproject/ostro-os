#!/usr/bin/env python
# Copyright (C) 2013 Intel Corporation
#
# Released under the MIT license (see COPYING.MIT)

# timeout decorator used by test case
# This provides the timeout mechansim for pyunit TC
# usage: @timeout(seconds)

"""Timeout Module"""
import sys
import signal
from functools import wraps
import unittest

class TimeOut(BaseException):
    """timeout expection"""
    pass

def timeout(seconds):
    """timeout decorator"""
    def decorator(fn):
        if hasattr(signal, 'alarm'):
            @wraps(fn)
            def wrapped_f(*args, **kw):
                current_frame = sys._getframe()
                def alarm_handler(signal, frame):
                    if frame is not current_frame:
                        raise TimeOut('%s seconds' % seconds)
                prev_handler = signal.signal(signal.SIGALRM, alarm_handler)
                try:
                    signal.alarm(seconds)
                    return fn(*args, **kw)
                finally:
                    signal.alarm(0)
                    signal.signal(signal.SIGALRM, prev_handler)
            return wrapped_f
        else:
            return fn
    return decorator

## get reference of wrapped_f code object
__TIMEOUT_CODE = timeout(1)(lambda: None).__code__
def hastimeout(func):
    """Return True if this func had added timeout decorator"""
    if hasattr(func, "__code__") and \
            getattr(func, "__code__") is __TIMEOUT_CODE:
        return True
    return False

def set_timeout(testsuite, seconds=None):
    """
    add timout to test case if it didn't have one,
    @param testsuite testsuite form loader()
    @param seconds: timeout seconds
    @return: updated testsuite
    """
    def _testset(testsuite):
        """interate tcs in testsuite"""
        for each in testsuite:
            if not isinstance(each, unittest.BaseTestSuite):
                yield each
            else:
                for each2 in _testset(each):
                    yield  each2

    if seconds:
        for tc in _testset(testsuite):
            assert hasattr(tc, "_testMethodName"), \
                "%s is not an unittest.TestCase object"
            testMethod = getattr(tc, tc._testMethodName)
            test_func = testMethod.im_func
            if not hastimeout(test_func):
                tc.run = timeout(seconds)(tc.run)
    return testsuite
