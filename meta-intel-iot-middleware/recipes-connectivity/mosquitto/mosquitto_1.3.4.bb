SUMMARY = "Open source MQTT v3.1 implemention"
DESCRIPTION = "Mosquitto is an open source (BSD licensed) message broker that implements the MQ Telemetry Transport protocol version 3.1. MQTT provides a lightweight method of carrying out messaging using a publish/subscribe model. "
HOMEPAGE = "http://mosquitto.org/"
SECTION = "console/network"
LICENSE = "BSD"
LIC_FILES_CHKSUM = "file://LICENSE.txt;md5=89aa5ea5f32e4260d84c5d185ee3add4"

DEPENDS = "openssl c-ares"

PR = "r0"

SRC_URI = "http://mosquitto.org/files/source/mosquitto-${PV}.tar.gz \
           file://build.patch \
           file://mosquitto.service \
"

SRC_URI[md5sum] = "9d729849efd74c6e3eee17a4a002e1e9"
SRC_URI[sha256sum] = "0a3982d6b875a458909c8828731da04772035468700fa7eb2f0885f4bd6d0dbc"


do_install() {
    oe_runmake install DESTDIR=${D}
    install -d ${D}${libbir}
    install -m 0644 lib/libmosquitto.a ${D}${libdir}/

    install -d ${D}${systemd_unitdir}/system/
    install -m 0644 ${WORKDIR}/mosquitto.service ${D}${systemd_unitdir}/system/

    cp ${D}${sysconfdir}/mosquitto/mosquitto.conf.example ${D}${sysconfdir}/mosquitto/mosquitto.conf
    sed 's/#user mosquitto/user root/' -i ${D}${sysconfdir}/mosquitto/mosquitto.conf
}

PACKAGES += "libmosquitto1 libmosquittopp1 ${PN}-clients ${PN}-python"

FILES_${PN} = "${sbindir}/mosquitto \
               ${bindir}/mosquitto_passwd \
               ${sysconfdir} \
               ${systemd_unitdir}/system/mosquitto.service \
"

FILES_libmosquitto1 = "${libdir}/libmosquitto.so.1"

FILES_libmosquittopp1 = "${libdir}/libmosquittopp.so.1"

FILES_${PN}-clients = "${bindir}/mosquitto_pub \
                       ${bindir}/mosquitto_sub \
"

FILES_${PN}-staticdev += "${libdir}/libmosquitto.a"

FILES_${PN}-python = "/usr/lib/python2.7/site-packages"

inherit systemd

SYSTEMD_SERVICE_${PN} = "mosquitto.service"
