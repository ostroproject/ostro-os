# Development tool - kernel command plugin
#
# Copyright (C) 2016 Intel Corporation
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""Devtool plugin containing the kernel subcommands"""

import os
import subprocess
import logging
import argparse
import glob
from bb.process import ExecutionError
from devtool import exec_build_env_command, setup_tinfoil, parse_recipe, DevtoolError
from devtool import standard

logger = logging.getLogger('devtool')

def kernel_menuconfig(args, config, basepath, workspace):
    """Entry point for the devtool 'kernel-menuconfig' subcommand"""

    # FIXME we end up with a triple parse here which is ugly (one for
    # the initial tinfoil instantiation, one for the modify, and then
    # finally one for the call to bitbake). Unfortunately it's
    # unavoidable without significant refactoring though so that will
    # have to wait until next release.

    tinfoil = setup_tinfoil(basepath=basepath)
    try:
        tinfoil.prepare(config_only=False)

        rd = parse_recipe(config, tinfoil, 'virtual/kernel', appends=True, filter_workspace=False)
        if not rd:
            return 1
        pn = rd.getVar('PN', True)
        # We need to do this carefully as the version will change as a result of running devtool modify
        ver = rd.expand('${EXTENDPE}${PV}-${PR}')
        taintfn = (rd.getVar('STAMP', True) + '.do_compile.taint').replace(ver, '*')
    finally:
        tinfoil.shutdown()

    if not pn in workspace:
        # FIXME this will break if any options are added to the modify
        # subcommand.
        margs = argparse.Namespace()
        margs.recipename = pn
        margs.srctree = None
        margs.wildcard = False
        margs.extract = True
        margs.no_extract = False
        margs.same_dir = False
        margs.no_same_dir = False
        margs.branch = 'devtool'
        standard.modify(margs, config, basepath, workspace)

    exec_build_env_command(config.init_path, basepath, 'bitbake -c menuconfig %s' % pn, watch=True)

    # Remove taint created by do_menuconfig, if any
    for fn in glob.glob(taintfn):
        os.remove(fn)

    return 0

def register_commands(subparsers, context):
    """Register devtool subcommands from the kernel plugin"""
    if context.fixed_setup:
        parser_menuconfig = subparsers.add_parser('kernel-menuconfig',
                                                  help='Allows altering the kernel configuration',
                                                  description='Ensures that the kernel source tree is in your workspace and then launches "make menuconfig" for the kernel',
                                                  group='advanced', order=-5)
        parser_menuconfig.set_defaults(func=kernel_menuconfig)
