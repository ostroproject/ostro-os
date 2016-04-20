import unittest
import re
import os
import string
from oeqa.oetest import oeRuntimeTest, skipModule
from oeqa.utils.decorators import *

def get_files_dir():
    """Get directory of supporting files"""
    pkgarch = oeRuntimeTest.tc.d.getVar('MACHINE', True)
    deploydir = oeRuntimeTest.tc.d.getVar('DEPLOY_DIR', True)
    return os.path.join(deploydir, "files", "target", pkgarch)

MAX_LABEL_LEN = 255
LABEL = "a" * MAX_LABEL_LEN

def setUpModule():
    if not oeRuntimeTest.hasPackage('security-manager'):
        skipModule(
            "security-manager module skipped: "
            "target doesn't have security-manager installed")

class SecurityManagerBasicTest(oeRuntimeTest):
    ''' base smack test '''
    def setUp(self):
        # TODO: avoid hardcoding path (also in SecurityManager itself)
        self.security_manager_db = '/usr/dbspace/.security-manager.db'
        cmd = "sqlite3 %s 'SELECT name from privilege ORDER BY privilege_id'" % self.security_manager_db
        status, output = self.target.run(cmd)
        self.assertFalse(status, msg="%s failed: %s" % (cmd, output))
        self.privileges = output.split()
        if not self.privileges:
            # Only privileges that map to a Unix group need to be known to
            # SecurityManager. Therefore it is possible that the query above
            # returns nothing. In that case, make up something for the tests.
            self.privileges.append('FoobarPrivilege')
        self.appid = 'test-app-id'
        self.pkgid = 'test-pkg-id'
        self.user = 'security-manager-user'
        idcmd = 'id -u %s' % self.user
        status, output = self.target.run(idcmd)
        if status:
            # -D is from busybox. It disables setting a password.
            createcmd = 'adduser -D %s' % self.user
            status, output = self.target.run(createcmd)
            self.assertFalse(status, msg="%s failed: %s" % (createcmd, output))
            status, output = self.target.run(idcmd)
        self.assertTrue(output.isdigit(), msg="Unexpected output from %s: %s" % (idcmd, output))
        self.uid = output

class SecurityManagerApp(SecurityManagerBasicTest):
    '''Tests covering app installation. Ordering is important, therefore tests are numbered.'''

    @skipUnlessPassed('test_ssh')
    def test_security_manager_01_setup(self):
        '''Check that basic SecurityManager setup is in place.'''
        # If we get this far, then at least the sqlite db must have been in place.
        # This does not mean much, but we need to start somewhere.
        pass

    @skipUnlessPassed('test_security_manager_01_setup')
    def test_security_manager_02_install(self):
        '''Test if installing an app sets up privilege rules for it, also in Cynara.'''
        self.target.copy_to(os.path.join(get_files_dir(), "app-runas"), "/tmp/")
        cmd = '/tmp/app-runas -a %s -p %s -u %s -r %s -i' % \
              (self.appid, self.pkgid, self.uid, self.privileges[0])
        status, output = self.target.run(cmd)
        self.assertFalse(status, msg="%s failed: %s" % (cmd, output))
        cmd = '''sqlite3 %s 'SELECT uid,app_name,pkg_name from app_pkg_view WHERE app_name = "%s"' ''' % \
              (self.security_manager_db, self.appid)
        status, output = self.target.run(cmd)
        self.assertFalse(status, msg="%s failed: %s" % (cmd, output))
        self.assertEqual(output, '|'.join((self.uid, self.appid, self.pkgid)))
        cmd = 'grep -r %s /var/cynara/db/' % self.appid
        status, output = self.target.run(cmd)
        self.assertFalse(status, msg="%s failed: %s" % (cmd, output))
        # User::App:: prefix still hard-coded here because it is not customizable at the moment.
        self.assertEqual(output, '/var/cynara/db/_MANIFESTS:User::App::%s;%s;%s;0xFFFF;' % \
                         (self.appid, self.uid, self.privileges[0]))

    @skipUnlessPassed('test_security_manager_02_install')
    def test_security_manager_03_run(self):
        '''Test running as app. Depends on preparations in test_security_manager_install().'''
        cmd = '''/tmp/app-runas -a %s -u %s -e -- sh -c 'id -u && cat /proc/self/attr/current' ''' % \
              (self.appid, self.uid)
        status, output = self.target.run(cmd)
        self.assertFalse(status, msg="%s failed: %s" % (cmd, output))
        self.assertEqual(output, '%s\nUser::App::%s' % (self.uid, self.appid))

    @skipUnlessPassed('test_security_manager_02_install')
    def test_security_manager_03_uninstall(self):
        '''Test removal of an app.'''
        cmd = '/tmp/app-runas -a %s -p %s -u %s -d' % \
              (self.appid, self.pkgid, self.uid)
        status, output = self.target.run(cmd)
        self.assertFalse(status, msg="%s failed: %s" % (cmd, output))
        cmd = '''sqlite3 %s 'SELECT uid,app_name,pkg_name from app_pkg_view WHERE app_name = "%s"' ''' % \
              (self.security_manager_db, self.appid)
        status, output = self.target.run(cmd)
        self.assertFalse(status, msg="%s failed: %s" % (cmd, output))
        # Entry does not really get removed. Bug filed here:
        # https://github.com/Samsung/security-manager/issues/2
        # self.assertEqual(output, '')
        cmd = 'grep -r %s /var/cynara/db/' % self.appid
        status, output = self.target.run(cmd)
        self.assertFalse(status, msg="%s failed: %s" % (cmd, output))
        # This also does not get removed. Perhaps same root cause.
        # self.assertEqual(output, '')
