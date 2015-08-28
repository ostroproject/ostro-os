#[PROTEXCAT]
#\License: ALL RIGHTS RESERVED
#\Author: Wang, Jing <jing.j.wang@intel.com>

import time
import subprocess
import os
from oeqa.oetest import oeRuntimeTest
import unittest

def tag(*args, **kwargs):
    """Decorator that adds attributes to classes or functions
    for use with the Attribute (-a) plugin.
    """
    def wrap_ob(ob):
        for name in args:
            setattr(ob, "tag__" + name, True)
        for name, value in kwargs.iteritems():
            setattr(ob, "tag__" + name, value)
        return ob
    return wrap_ob

def gettag(obj, key, default=None):
    key = "tag__" + key
    if not isinstance(obj, unittest.TestCase):
        return getattr(obj, key, default)
    tc_method = getattr(obj, obj._testMethodName)
    tc_class = tc_method.__self__.__class__
    ret = getattr(tc_method, key, getattr(tc_class, key, getattr(obj, key, default)))
    return ret

def shell_cmd(cmd):
    """Execute shell command till it return"""
    cmd_proc = subprocess.Popen(cmd, shell=True)
    return cmd_proc.wait() if cmd_proc else -1

def shell_cmd_timeout(cmd, timeout=0):
    """Execute shell command till timeout"""
    cmd_proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    if not cmd_proc:
        return -1, ''
    t_timeout, tick = timeout, 2
    ret, output = None, ''
    while True:
        time.sleep(tick)
        output = cmd_proc.communicate()[0]
        ret = cmd_proc.poll()
        if ret is not None:
            break

        if t_timeout > 0:
            t_timeout -= tick

        if t_timeout <= 0:
            # timeout, kill command
            cmd_proc.kill()
            ret = -99999
            break
    return ret, output

def collect_pnp_log(casename, logname, log):
    """collect the result log for pnp part"""
    curpath = os.getcwd()
    if not os.path.exists(casename):
        os.makedirs(casename)

    logpath = os.path.join(curpath, casename, logname)
    logtime = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(logpath, "a") as text_file:
        text_file.write("%s %s:%s\n" %(logtime, casename, log))

def get_files_dir():
    """Get directory of supporting files"""
    pkgarch = oeRuntimeTest.tc.d.getVar('MACHINE', True)
    deploydir = oeRuntimeTest.tc.d.getVar('DEPLOY_DIR', True)
    return os.path.join(deploydir, "files", pkgarch)

def get_native_dir():
    """Get directory of native files"""
    arch = oeRuntimeTest.tc.d.getVar('BUILD_ARCH', True)
    deploydir = oeRuntimeTest.tc.d.getVar('DEPLOY_DIR', True)
    return os.path.join(deploydir, "files", "native", arch)

