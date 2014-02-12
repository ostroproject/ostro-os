DESCRIPTION = "Transparently implements the necessary message formats and transport security as well as device registration"
HOMEPAGE = "http://enableiot.com"
LICENSE = "BSD-2-Clause & BSD-3-Clause & GPL-2.0 & Apache-2.0 & MIT & PD"

LIC_FILES_CHKSUM = "file://LICENSE;md5=939d32aa04ac243eeecd833bb19644ef"


DEPENDS = "nodejs"

SRC_URI = "file://iotkit-agent-1.1.0.tar.bz2 \
           file://iotkit-agent-deps-0.1.tar.bz2 \
           file://iotkit-agent"

SRC_URI[md5sum] = "ad4859c184b80c1074befe83892103af"
SRC_URI[sha256sum] = "8ea155f0bcf5742b9e3295193b25c46b926a79c4"

do_install () {
          install -d ${D}${libdir}
          install -d ${D}${libdir}/node_modules/
          install -d ${D}${libdir}/node_modules/iotkit-agent/

          cp -r ${WORKDIR}/iotkit-agent-deps-0.1/* ${D}${libdir}/node_modules/
          cp -r ${S}/* ${D}${libdir}/node_modules/iotkit-agent/
          #chmod -R 0644 ${D}${libdir}/node_modules/
          chmod 0755 ${D}${libdir}/node_modules/forever/bin/forever

          install -d ${D}${sysconfdir}/init.d/
          install -m 0755 ${WORKDIR}/iotkit-agent ${D}${sysconfdir}/init.d/
}

inherit update-rc.d

INITSCRIPT_NAME = "iotkit-agent"
INITSCRIPT_PARAMS = "defaults 99"

FILES_${PN} = "${libdir}/node_modules/ \
               ${sysconfdir}/init.d/"
