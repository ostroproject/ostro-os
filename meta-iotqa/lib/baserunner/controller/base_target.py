#!/usr/bin/env python
# Copyright (C) 2013 Intel Corporation
#
# Released under the MIT license (see COPYING.MIT)

# Base target module used by target supported testrunner
# This provides TC the capability to access target DUT

"""Base Target Module"""
from abc import ABCMeta, abstractmethod

class BaseTarget(object):
    """abstract base target class"""
    __metaclass__ = ABCMeta
    def __init__(self):
        self.connection = None

    @abstractmethod
    def start(self, params=None):
        """setup the bridge connection to target"""
        pass

    @abstractmethod
    def stop(self):
        """shutdown the bridge connection to target"""
        pass

    def restart(self, params=None):
        """restart the bridge to target"""
        self.stop()
        self.start(params)

    def run(self, cmd, timeout=None):
        """execute command via bridge"""
        if self.connection:
            return self.connection.run(cmd, timeout)
        return True

    def copy_to(self, localpath, remotepath):
        """copy local file to target"""
        return self.connection.copy_to(localpath, remotepath)

    def copy_from(self, remotepath, localpath):
        """copy file from target to local"""
        return self.connection.copy_from(remotepath, localpath)
