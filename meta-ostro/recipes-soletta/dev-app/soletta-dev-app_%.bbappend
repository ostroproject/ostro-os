# Do not start the systemd-dev-app services by default. To enable them, log in
# to the system and enable soletta-dev-app-server.service and
# soletta-dev-app-avahi-discover.service.

SYSTEMD_AUTO_ENABLE_${PN} = "disable"

FILESEXTRAPATHS_prepend := "${THISDIR}/files:"

SRC_URI += " file://0001-Add-firewall-rules-to-allow-access.patch"

RDEPENDS_${PN} += " iptables"

do_install_prepend() {
    rm -rf ${S}/patches
}
