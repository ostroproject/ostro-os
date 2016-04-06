#[PROTEXCAT]
#\License: ALL RIGHTS RESERVED
#\Author: Wang, Jing <jing.j.wang@intel.com>

import time
import subprocess
import os
import sys
from oeqa.oetest import oeRuntimeTest
import unittest

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
    return os.path.join(deploydir, "files", "target", pkgarch)

def get_native_dir():
    """Get directory of native files"""
    arch = oeRuntimeTest.tc.d.getVar('BUILD_ARCH', True)
    deploydir = oeRuntimeTest.tc.d.getVar('DEPLOY_DIR', True)
    return os.path.join(deploydir, "files", "native", arch)

def add_group(groupname, gid=None, target=None):
    target = target if target is not None else oeRuntimeTest.tc.target
    (ret, output) = target.run("groupadd %s %s"%(groupname, "" if gid is None else "-g %s"%gid))
    print >> sys.stderr, output
    return ret == 0

def add_user(username, group=None, home_dir=None, target=None):
    target = target if target is not None else oeRuntimeTest.tc.target
    cmd = "useradd "
    if group is not None:
        (ret, output) = target.run("cat /etc/group | grep %s"%group)
        if ret != 0:
            if not add_group(group, target=target):
                return False
        cmd = cmd + "-g %s "%group
    if home_dir is None:
        home_dir = "/home/%s"%username
    target.run("mkdr -p %s"%home_dir)
    cmd = cmd + "-d %s "%home_dir
    cmd = cmd + username
    (ret, output) = target.run(cmd)
    print >> sys.stderr, output
    return ret == 0

def remove_user(username, target=None):
    target = target if target is not None else oeRuntimeTest.tc.target
    return target.run("userdel %s"%username)[0] == 0

def escape(s):
    ret = s.replace(r'"', r'\"')
    return ret

def run_as(username, cmd, timeout=None, target=None, need_escape=True):
    """
    escape: if True, run_as will try to escape some special char. for example: '"$
    """
    target = target if target is not None else oeRuntimeTest.tc.target
    cmd = escape(cmd) if need_escape else cmd
    cmd = "su %s -c \"%s\""%(username, cmd)
    return target.run(cmd, timeout) if timeout else target.run(cmd)
    

