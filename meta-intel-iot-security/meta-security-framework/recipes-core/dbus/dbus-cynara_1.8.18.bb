require dbus-oe-core.inc
FILESEXTRAPATHS_prepend := "${COREBASE}/meta/recipes-core/dbus/dbus:${THISDIR}/dbus-cynara:"
S = "${WORKDIR}/dbus-${PV}"
libexecdir = "${libdir}/dbus"

SRC_URI[md5sum] = "83e607e9ccb1c921d5b6bbea2376a36c"
SRC_URI[sha256sum] = "36f2eb9c777a3c71562573da36a147e900a642afcd44d2b0470d992a4898c4f2"

# From https://review.tizen.org/gerrit/#/admin/projects/platform/upstream/dbus
# revision 6c9997fb1cdff4281166e8c2fb8276018b1025dd
# aka https://review.tizen.org/git/?p=platform%2Fupstream%2Fdbus.git;a=shortlog;h=refs%2Fheads%2Fsandbox%2Fjacekbe%2Fupgrade
# as announced in https://bugs.tizen.org/jira/browse/TC-2520 "D-Bus: local denial of service attack"
SRC_URI += " \
file://0001-Fix-memleak-in-GetConnectionCredentials-handler.patch \
file://0002-New-a-sv-helper-for-using-byte-arrays-as-the-variant.patch \
file://0003-Add-LSM-agnostic-support-for-LinuxSecurityLabel-cred.patch \
file://0004-Integration-of-Cynara-asynchronous-security-checks.patch \
file://0005-Disable-message-dispatching-when-send-rule-result-is.patch \
file://0006-Handle-unavailability-of-policy-results-for-broadcas.patch \
file://0007-Add-own-rule-result-unavailability-handling.patch \
"

# Provides a legacy API which shouldn't be used in new code. It is
# still needed at the moment because cynara helper methods call it
# (creds-dbus-inner.cpp, creds-gdbus.cpp).
SRC_URI += "file://0008-Add-GetConnectionSmackContext-D-Bus-daemon-method.patch"

# Depends on special Cynara rules which get installed in the
# security-manager-policy package. From patch set 5 in:
# https://review.tizen.org/gerrit/#/c/31310/ 
SRC_URI += "file://Perform-Cynara-runtime-policy-checks-by-default.patch"

DEPENDS += "cynara smack"
EXTRA_OECONF += "--enable-cynara"

# Only the main package gets created here, everything else remains in the
# normal dbus recipe.
do_install_append () {
    for i in ${@' '.join([d.getVar('D', True) + x for x in (' '.join([d.getVar('FILES_dbus-cynara-' + p, True) or '' for p in ['lib', 'dev', 'staticdev', 'doc', 'locale', 'ptest']])).split()])}; do
        rm -rf $i
    done

    # Try to remove empty directories, starting with the
    # longest path (= deepest directory) first.
    # Find needs a valid current directory. Somehow the directory
    # we get called in is gone by the time that we get invoked.
    ( cd ${D}
      for i in `find . -type d | sort -r`; do
        rmdir $i || true
      done
    )
}

# Avoid warning about dbus and dbus-cynara providing dbus-x11.
RPROVIDES_${PN}_remove = "${OLDPKGNAME}"
