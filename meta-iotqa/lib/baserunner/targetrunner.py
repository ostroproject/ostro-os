#!/usr/bin/env python
# Copyright (C) 2013 Intel Corporation
#
# Released under the MIT license (see COPYING.MIT)

# test runner which support run testing on target device

"""test runner for target device"""
import sys
from optparse import make_option
from baserunner import TestRunnerBase

class TargetTestRunner(TestRunnerBase):
    '''test runner which support target DUT access'''
    def __init__(self, context=None):
        super(TargetTestRunner, self).__init__(context)
        self.option_list.extend([
            make_option("-c", "--controller", dest="controller",
                    help="the target controller to bridge host and target")])

    def _get_arg_val(self, dest_name, store_val=True):
        '''get arg value from testrunner args'''
        args = sys.argv
        for opt in self.option_list:
            if opt.dest == dest_name:
                arg_names = opt._short_opts + opt._long_opts
                break
        else:
            return None

        for cur_arg in arg_names:
            try:
                ind = args.index(cur_arg)
                return args[ind+1] if store_val else True
            except:
                pass
        return None

    def configure(self, options):
        '''configure before testing'''
        super(TargetTestRunner, self).configure(options)
        print "configure target test runner"

if __name__ == "__main__":
    runner = TargetTestRunner()
    runner.configure(runner.get_options())
    suite = runner.filtertest(runner.loadtest())
    print "Found %s tests" % suite.countTestCases()
    runner.start(suite)
