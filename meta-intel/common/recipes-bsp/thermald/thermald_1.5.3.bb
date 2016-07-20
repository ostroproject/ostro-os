SUMMARY = "Linux thermal daemon"

DESCRIPTION = "Thermal Daemon is a Linux daemon used to prevent the \
overheating of platforms. This daemon monitors temperature and applies \
compensation using available cooling methods."

HOMEPAGE = "https://github.com/01org/thermal_daemon"

DEPENDS = "dbus dbus-glib libxml2 glib-2.0"
DEPENDS += "${@bb.utils.contains('DISTRO_FEATURES','systemd','systemd','',d)}"

LICENSE = "GPL-2.0"
LIC_FILES_CHKSUM = "file://COPYING;md5=ea8831610e926e2e469075b52bf08848"

SRC_URI = "https://github.com/01org/thermal_daemon/archive/v${PV}.tar.gz"
SRC_URI[md5sum] = "66402236ed3c86a798029cb4d5313817"
SRC_URI[sha256sum] = "e20b450ef27a5b5e45474c831663c8f5ecd14c82ace5a4b1e06c442e0a23b53e"

S = "${WORKDIR}/thermal_daemon-${PV}"

inherit pkgconfig autotools systemd

FILES_${PN} += "${datadir}/dbus-1/system-services/*.service"

SYSTEMD_SERVICE_${PN} = "thermald.service"

COMPATIBLE_HOST = '(i.86|x86_64).*-linux'

CONFFILES_${PN} = " \
                   ${sysconfdir}/thermald/thermal-conf.xml \
                   ${sysconfdir}/thermald/thermal-cpu-cdev-order.xml \
                  "
