#!/usr/bin/env python
# Copyright (C) 2013 Intel Corporation
#
# Released under the MIT license (see COPYING.MIT)

# Log module used by base testrunner
# It catch stdout and stderr to a new local file

"""
log module
"""
import os, sys

class MultipleCall(object):
    """It's a wraper, if this obj was called, it will call
    all objs' method and return the firstObj's result
    """
    def __init__(self, streams, func):
        self.streams = streams
        self.func = func

    def __call__(self, *args, **kwargs):
        """call func and return result of the first stream's method"""
        return [getattr(x, self.func)(*args, **kwargs) for x in\
                   self.streams][0]

class Tee(object):
    """Tee is a file distributer to apply call to all streams"""
    def __init__(self, *args):
        self.streams = list(args)
        self.old_stream = self.streams[0]

    def __getattr__(self, name):
        if hasattr(self.old_stream, name):
            if callable(getattr(self.old_stream, name)):
                return MultipleCall(self.streams, name)
            return getattr(self.old_stream, name)
        return getattr(self.streams, name)

    def close(self, start=1, end=None):
        """close streams"""
        MultipleCall(self.streams[start:end], "close")()
        del self.streams[start:end]

class LogHandler(object):
    """log hander"""
    def __init__(self, dirpath):
        """
        @para dirpath: the output dir for log file
        """
        self.dirpath = dirpath
        self.tee_std = None
        self.tee_err = None
        self.output = None

    def start(self):
        """start catch output to log file"""
        self.output = open(os.path.join(self.dirpath, "output.log"), "w")
        self.tee_std = sys.stdout if isinstance(sys.stdout, Tee) else \
                         Tee(sys.stdout)
        self.tee_err = sys.stderr if isinstance(sys.stderr, Tee) else \
                         Tee(sys.stderr)
        self.tee_std.append(self.output)
        self.tee_err.append(self.output)
        sys.stdout = self.tee_std
        sys.stderr = self.tee_err

    def end(self):
        """close log file"""
        sys.stdout.close()
        sys.stderr.close()
        sys.stdout = self.tee_std.old_stream
        sys.stderr = self.tee_err.old_stream

# redirect stdout and stderr to a Tee object
sys.stdout = Tee(sys.stdout)
sys.stderr = Tee(sys.stderr)

