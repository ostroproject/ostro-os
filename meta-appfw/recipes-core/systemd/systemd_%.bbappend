FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

# We want/need systemd-networkd
PACKAGECONFIG += "iptc networkd"
DEPENDS += "iptables"

# Patch systemd-nspawn to
#   - delay binary/OS-tree check after mounts
#   - support starting DHCP client in non-system containers
SYSTEMD_228_PATCHES = " \
    file://228/0001-nspawn-don-t-check-binary-OS-tree-before-all-mounts-.patch \
    file://228/0002-nspawn-added-support-for-starting-DHCP-client-in-non.patch \
"

SRC_URI += "${SYSTEMD_228_PATCHES}"

# systemd-nspawn needs getent (from glibc).
RDEPENDS_${PN} += "glibc-getent"
