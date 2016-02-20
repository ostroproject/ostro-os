DESCRIPTION = "Bluetooth rfkill event daemon for Bluetooth chips"
SECTION = "connectivity"

LICENSE = "GPLv2"
LIC_FILES_CHKSUM = "file://${THISDIR}/COPYING;md5=3fa94220fac4e7b1463e6fd8d63140c5"

DEPENDS = "glib-2.0 bluez5"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

inherit systemd

SYSTEMD_SERVICE_${PN} = "bluetooth-rfkill-event.service"

SRC_URI = "file://bluetooth_rfkill_event.c \
           file://bluetooth-rfkill-event.service \
           file://bcm43341.conf"

S = "${WORKDIR}"

INC_DIRS = "-I${STAGING_INCDIR}/glib-2.0 -I${STAGING_LIBDIR}/glib-2.0/include/"

LIBS = "-lglib-2.0"

do_compile() {
        ${CC} $CFLAGS -o bluetooth_rfkill_event bluetooth_rfkill_event.c ${INC_DIRS} ${LIBS}
}

do_install() {
        install -v -d ${D}${sbindir}
        install -m 0755 bluetooth_rfkill_event ${D}${sbindir}

        if ${@base_contains('DISTRO_FEATURES','systemd','true','false',d)}; then
                # Copy file service
                install -d ${D}/${systemd_unitdir}/system
                install -m 644 ${WORKDIR}/bluetooth-rfkill-event.service ${D}/${systemd_unitdir}/system
        fi

        install -v -d  ${D}/etc/firmware/
        install -m 0755 ${WORKDIR}/bcm43341.conf ${D}/etc/firmware/bcm43341.conf
}
