FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

# Most patches from sandbox/jobol/v219. Cannot be applied unconditionally
# because systemd panics when booted without Smack support:
# systemd[1]: Cannot determine cgroup we are running in: No such file or directory
# systemd[1]: Failed to allocate manager object: No such file or directory
# [!!!!!!] Failed to allocate manager object, freezing.
#
# There's a slight dependency on the base systemd in 0005-tizen-smack-Handling-network.
# We use the beginning of PV (unexpanded here to prevent a cyclic dependency
# during resolution apparently caused by ${SRCPV}) to pick the right set of
# patches.
#
# Patches are optional. Hopefully we won't need any for systemd >= 229.
SRC_URI_append_smack = " ${@d.getVar('SYSTEMD_SMACK_PATCHES_' + d.getVar('PV', False)[0:3], True) or ''}"

SYSTEMD_SMACK_PATCHES_216 = " \
file://0003-tizen-smack-Handling-of-run-and-sys-fs-cgroup-v216.patch \
file://0004-tizen-smack-Handling-of-dev-v216.patch \
file://0005-tizen-smack-Handling-network-v216.patch \
file://0006-tizen-smack-Tuning-user-.service.m4.in-v216.patch \
file://0007-tizen-smack-Runs-systemd-journald-with-v216.patch \
"

SYSTEMD_SMACK_PATCHES_219 = " \
file://0003-tizen-smack-Handling-of-run-and-sys-fs-cgroup.patch \
file://0004-tizen-smack-Handling-of-dev.patch \
file://0005-tizen-smack-Handling-network.patch \
file://0006-tizen-smack-Tuning-user-.service.m4.in.patch \
file://0007-tizen-smack-Runs-systemd-journald-with.patch \
"
SYSTEMD_SMACK_PATCHES_225 = " \
file://0003-tizen-smack-Handling-of-run-and-sys-fs-cgroup.patch \
file://0004-tizen-smack-Handling-of-dev.patch \
file://0005-tizen-smack-Handling-network-v225.patch \
file://0006-tizen-smack-Tuning-user-.service.m4.in.patch \
file://0007-tizen-smack-Runs-systemd-journald-with.patch \
"

# TODO: 0006-tizen-smack-Tuning-user-.service.m4.in.patch must be re-evaluated
# in combination with user session handling via PAM (should set SmackProcessLabel=User),
# D-Bus 1.10 per-user sessions (should set DBUS_SESSION_BUS_ADDRESS, currently
# pending for merging into OE-core master). Capability handling probably belongs into
# some application framework layer, it is not specific to core Smack support.
SYSTEMD_SMACK_PATCHES_228 = " \
file://0005-tizen-smack-Handling-network-v228.patch \
file://0006-tizen-smack-Tuning-user-.service.m4.in.patch \
file://mount-setup.c-fix-handling-of-symlink-Smack-labellin-v228.patch \
"

# From Tizen .spec file.
EXTRA_OECONF_append_smack = " --with-smack-run-label=System"

install_file() {
    install -d $(dirname $1)
    cat >>$1
    chmod ${2:-0644} $1
}

# We need to emulate parts of the filesystem permissions from Tizen here.
# The part for regular files is in base-files.bbappend, but /var/log and
# /var/tmp point into /var/volatile (tmpfs) and get created anew during
# startup. We set these permissions directly after creating them via
# /etc/tmpfiles.d/00-create-volatile.conf
RDEPENDS_${PN}_append_smack = " smack-userspace"
do_install_append_smack() {
    install_file ${D}${systemd_unitdir}/system/systemd-tmpfiles-setup.service.d/smack.conf <<EOF
[Service]
ExecStartPost=/bin/sh -c '([ ! -d /var/tmp ] || chsmack -L -a \"*\" /var/tmp) && ([ ! -d /var/log ] || chsmack -L -a System::Log /var/log && chsmack -L -t /var/log)'
EOF

    # Mount /tmp publicly accessable. Based on patch by Michael Demeter <michael.demeter@intel.com>.
    # Upstream systemd temporarily had SmackFileSystemRoot for this (https://github.com/systemd/systemd/pull/1664),
    # but it was removed again (https://github.com/systemd/systemd/issues/1696) because
    # util-linux mount will ignore smackfsroot when Smack is not active. However,
    # busybox is not that intelligent.
    #
    # When using busybox mount, adding smackfsroot=* and booting without
    # Smack (i.e. security=none), tmp.mount will fail with an error about
    # "Bad mount option smackfsroot".
    install_file ${D}${systemd_unitdir}/system/tmp.mount.d/smack.conf <<EOF
[Mount]
Options=smackfsroot=*
EOF

    # Run systemd-journald with the hat ("^") Smack label.
    #
    # The journal daemon needs global read access to gather information
    # about the services spawned by systemd. The hat label is intended
    # for this purpose. The journal daemon is the only part of the
    # System domain that needs read access to the User domain. Giving
    # the journal daemon the hat label means that we can remove the
    # System domain's read access to the User domain.
    #
    # Original author: Casey Schaufler <casey@schaufler-ca.com>
    #
    # This is considered a configuration change and thus distro specific.
    install_file ${D}${systemd_unitdir}/system/systemd-journald.service.d/smack.conf <<EOF
[Service]
SmackProcessLabel=^
EOF
}

# Will get installed in ${sysconfdir}/udev/rules.d/ by base systemd recipe.
SRC_URI += "file://udev-smack-default.rules"

# A workaround for a missing space in a SRC_URI_append in a private layer elsewhere:
SRC_URI += ""

# Maintaining trivial, non-upstreamable configuration changes as patches
# is tedious. But in same cases (like early mounting of special directories)
# the configuration has to be in code. We make these changes here directly.
do_patch[prefuncs] += "patch_systemd"
do_patch[vardeps] += "patch_systemd"
patch_systemd() {
    # Handling of /run and /sys/fs/cgroup. Make /run a transmuting directory to
    # enable systemd communications with services in the User domain.
    # Original patch by Michael Demeter <michael.demeter@intel.com>.
    #
    # We simplify the patching by touching only lines which check the result of
    # mac_smack_use(). Those are the ones which are used when Smack is active.
    #
    # smackfsroot=* on /sys/fs/cgroup may be upstreamable, but smackfstransmute=System::Run
    # is too distro specific (depends on Smack rules) and thus has to remain here.
    sed -i -e 's;\("/sys/fs/cgroup", *"[^"]*", *"[^"]*\)\(.*mac_smack_use.*\);\1,smackfsroot=*\2;' \
           -e 's;\("/run", *"[^"]*", *"[^"]*\)\(.*mac_smack_use.*\);\1,smackfstransmute=System::Run\2;' \
           ${S}/src/core/mount-setup.c
}
