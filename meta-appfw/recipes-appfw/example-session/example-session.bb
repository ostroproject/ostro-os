DESCRIPTION = "Example TLM session file for launching example-app"
HOMEPAGE = "http://github.com/01org/iot-app-fw"
LICENSE = "BSD-3-Clause"

LIC_FILES_CHKSUM = "file://COPYING.MIT;md5=838c366f69b72c5df05c96dff79b35f2"

SRC_URI = "file://example-corp.ini \
           file://example-corp.service \
           file://COPYING.MIT"

IOTAPP_PROVIDER = "example-corp"
IOTAPP_SERVICE_FILE_PATH = "${systemd_unitdir}/system/example-corp.service"
IOTAPP_TLM_SESSION_FILE_PATH = "/etc/session.d/example-corp.ini"

# automatically start the service during boot
SYSTEMD_SERVICE_${PN} = "example-corp.service"

RDEPENDS_${PN} += "example-app"

inherit iot-app systemd

S = "${WORKDIR}"
INHIBIT_PACKAGE_DEBUG_SPLIT = "1"

# TODO: figure out a suitable target for installing the service link
do_install() {
    mkdir -p ${D}/lib/systemd/system
    mkdir -p ${D}/etc/session.d

    install example-corp.service ${D}${systemd_unitdir}/system/example-corp.service
    install example-corp.ini ${D}/etc/session.d/example-corp.ini

    # we did not need to install any files to private path
    rmdir -p --ignore-fail-on-non-empty ${D}${IOTAPP_INSTALLATION_PATH}
}

FILES_${PN} += "${systemd_unitdir}/system/example-corp.service"
