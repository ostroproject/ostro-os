SUMMARY = "Systemd service that brings up the CAN service at boot time"
AUTHOR = "Kevron Rees"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE;md5=838c366f69b72c5df05c96dff79b35f2"
PR = "r1"

inherit systemd

SRC_URI = "file://start-can \
           file://can-init \
           file://can-init.service \
           file://LICENSE \
          "

S = "${WORKDIR}"

SYSTEMD_PACKAGES = "${PN}"
SYSTEMD_SERVICE_${PN} = "can-init.service"


do_install() {
        install -d ${D}/${bindir}
        install -d ${D}/${systemd_unitdir}/system
        install -d ${D}/etc
        install -m 0755 ${S}/start-can ${D}/${bindir}/start-can
        install -m 0644 ${S}/can-init.service ${D}/${systemd_unitdir}/system/can-init.service
        install -m 0644 ${S}/can-init ${D}/etc/can-init
}

FILES_${PN} = " \
               ${bindir}/start-can \
               ${systemd_unitdir}/system/can-init.service \
               /etc/can-init \
              "


RDEPENDS_${PN}_class-native = ""
RDEPENDS_${PN} += " iproute2 "
