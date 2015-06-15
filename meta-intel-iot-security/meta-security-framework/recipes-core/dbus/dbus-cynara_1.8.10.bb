require recipes-core/dbus/dbus.inc
FILESEXTRAPATHS_prepend := "${COREBASE}/meta/recipes-core/dbus/dbus:${THISDIR}/dbus:"
S = "${WORKDIR}/dbus-${PV}"
libexecdir = "${libdir}/dbus"

SRC_URI[md5sum] = "6be5ef99ae784de9d04589eb067fe038"
SRC_URI[sha256sum] = "10bf87fdb68815edd01d53885101dbcdd80dacad7198912cca61a4fa22dfaf8e"

# From https://review.tizen.org/gerrit/#/admin/projects/platform/upstream/dbus
# revision 9e77cdf01b73de313b360290ca0987410e04c082
# aka https://review.tizen.org/gerrit/#/c/31310/
#
# Rebased onto 1.8.10 because that is the version in OE Fido.
# Should coordinate (and redo) rebasing with the Samsung maintainers of the
# D-Bus Cynara patches, see https://bugs.tizen.org/jira/browse/TC-2520
SRC_URI += " \
file://0001-Enable-checking-of-smack-context-from-DBus-interface.patch \
file://0002-Enforce-smack-policy-from-conf-file.patch \
file://0003-Set-error-when-message-delivery-is-denied-due-to-rec.patch \
file://0004-GetConnectionCredentials-add-smack-support.patch \
file://0005-policy-add-check-element.patch \
file://0006-Integration-of-asynchronous-security-checks.patch \
file://0007-Disable-message-dispatching-when-send-rule-result-is.patch \
file://0008-Handle-receive-rule-result-unavailability-and-messag.patch \
file://0009-Add-check-own-.-support.patch \
file://0010-Fix-several-BusResult-dbus_bool_t-mismatches.patch \
file://0011-Do-not-rely-on-Cynara-cache-when-processing-check-ru.patch \
file://0013-various-compile-fixes.patch \
"

# Depends on special Cynara rules which get installed in the
# security-manager-policy package.
SRC_URI += "file://0012-Perform-Cynara-runtime-policy-checks-by-default.patch"

DEPENDS += "cynara smack"
EXTRA_OECONF += "--enable-cynara --enable-smack"

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
