# Creates a package containing a systemd configuration entry
# for the watchdog feature. Activate the watchdog by including
# the package in the image.

LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

inherit allarch

do_install () {
    install -d ${D}/${sysconfdir}/systemd/system.conf.d
    echo "RuntimeWatchdogSec=90" >${D}/${sysconfdir}/systemd/system.conf.d/00-runtime-watchdog.conf
}

CONFFILES_${PN} = "${sysconfdir}/systemd/system.conf.d/00-runtime-watchdog.conf"
