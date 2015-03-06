FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

# Additional systemd patches from Tizen 3.0 (accepted/tizen/mobile/20150208.065204-0-g1c6d7a3).
SRC_URI += " \
file://0001-add-install_service-macro.patch \
file://0002-define-_unitdir_user-macro-for-user-session-units.patch \
file://0003-Allow-swap-to-be-activated-concurrently-with-sysinit.patch \
file://0004-systemd-upgrade-Import-platform-restart-from-RSA.patch \
file://0005-Smack-enabled-systems-need-dev-special-devices-corre.patch \
file://0006-Smack-sharing-of-run.patch \
file://0007-Set-Smack-ambient-to-match-run-label.patch \
file://0008-Set-Smack-netlabel-host-rules.patch \
file://0009-execute-add-SmackExecLabel-key-for-services.patch \
file://0010-user-.service-use-the-SmackExecLabel-key.patch \
file://0011-logind-spawn-user-instance-after-saving-user-data.patch \
file://0012-Run-systemd-journald-with-the-hat-Smack-label.patch \
file://0013-55-udev-smack-default.rules-updated-for-systemd-212.patch \
file://0014-Set-DBUS_SESSION_BUS_ADDRESS-for-user-instance.patch \
file://0015-logind-mount-per-user-tmpfs-with-smackfsroot-for-sma.patch \
file://0016-journald-add-CAP_MAC_OVERRIDE-in-journald-for-SMACK-.patch \
file://0020-Start-the-user-session-with-capabilities-for-setting.patch \
file://0021-Add-inheritable-CAP_MAC_OVERRIDE-to-user-session.patch \
file://0022-smack-Don-t-follow-symbolic-links-for-setting-smack-.patch \
"

# Do not apply. They reduce the number of pre-defined users. Probably
# needs to be solved differently when building with bitbake.
# file://0017-networkd-disable-tmpfiles-and-sysusers-bits-associat.patch
# file://0018-journal-remote-do-not-install-tmpfiles-and-sysusers-.patch
# file://0023-build-sys-configure-the-list-of-system-users.patch

# Does not apply, and misnamed anyway. What it does is adding "session  optional pam_systemd.so"
# to src/login/systemd-user.
# file://0019-Update-to-216-with-conditional-kdbus-support.patch

# Does not apply.
# file://0024-tmpfiles-make-resolv.conf-entry-conditional-on-resol.patch

# From Tizen .spec file.
EXTRA_OECONF += "--with-smack-run-label=System"

# We need to emulate parts of the filesystem permissions from Tizen here.
# The part for regular files is in base-files.bbappend, but /var/log and
# /var/tmp point into /var/volatile (tmpfs) and get created anew during
# startup. We set these permissions directly after creating them via
# /etc/tmpfiles.d/00-create-volatile.conf
RDEPENDS_${PN}_append = " smack-userspace"
do_install_append() {
    # sed did weird things for this replacement (duplicated ExecStart), works with perl.
    perl -pi -e "s@^ExecStart=(.*)@ExecStart=\\1\\nExecStartPost=/bin/sh -c '([ ! -d /var/tmp ] || chsmack -L -a \"*\" /var/tmp) && ([ ! -d /var/log ] || chsmack -L -a System::Log /var/log && chsmack -L -t /var/log)'@" ${D}${systemd_unitdir}/system/systemd-tmpfiles-setup.service
}
