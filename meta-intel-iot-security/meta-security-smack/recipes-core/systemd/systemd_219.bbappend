FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

# From sandbox/jobol/v219. Cannot be applied unconditionally
# because systemd panics when booted without Smack support:
# systemd[1]: Cannot determine cgroup we are running in: No such file or directory
# systemd[1]: Failed to allocate manager object: No such file or directory
# [!!!!!!] Failed to allocate manager object, freezing.
SRC_URI_append_smack = " \
file://0001-tizen-rpm-2-useful-macro-for-RPM.patch \
file://0002-tizen-smack-Handling-of-tmp.patch \
file://0003-tizen-smack-Handling-of-run-and-sys-fs-cgroup.patch \
file://0004-tizen-smack-Handling-of-dev.patch \
file://0005-tizen-smack-Handling-network.patch \
file://0006-tizen-smack-Tuning-user-.service.m4.in.patch \
file://0007-tizen-smack-Runs-systemd-journald-with.patch \
"

# Not applied.
# Used to be 0019-Update-to-216-with-conditional-kdbus-support.patch
# in the Tizen patches for 2.12.
# 0008-tizen-Add-pam_systemd.so-to-systemd-user.patch

# Not applied because not related to Smack.
# 0009-tizen-Tune-of-swap.patch

# From Tizen .spec file.
EXTRA_OECONF_append_smack = " --with-smack-run-label=System"

# We need to emulate parts of the filesystem permissions from Tizen here.
# The part for regular files is in base-files.bbappend, but /var/log and
# /var/tmp point into /var/volatile (tmpfs) and get created anew during
# startup. We set these permissions directly after creating them via
# /etc/tmpfiles.d/00-create-volatile.conf
RDEPENDS_${PN}_append_smack = " smack-userspace"
do_install_append_smack() {
    # sed did weird things for this replacement (duplicated ExecStart), works with perl.
    perl -pi -e "s@^ExecStart=(.*)@ExecStart=\\1\\nExecStartPost=/bin/sh -c '([ ! -d /var/tmp ] || chsmack -L -a \"*\" /var/tmp) && ([ ! -d /var/log ] || chsmack -L -a System::Log /var/log && chsmack -L -t /var/log)'@" ${D}${systemd_unitdir}/system/systemd-tmpfiles-setup.service
}
