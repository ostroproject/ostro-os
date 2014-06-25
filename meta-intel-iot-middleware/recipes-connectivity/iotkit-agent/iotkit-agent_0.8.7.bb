DESCRIPTION = "Transparently implements the necessary message formats and transport security as well as device registration"
HOMEPAGE = "http://enableiot.com"
LICENSE = "BSD-2-Clause & BSD-3-Clause & GPL-2.0 & Apache-2.0 & MIT & PD"

LIC_FILES_CHKSUM = "file://LICENSE;md5=30c8ae0368f724cf5f753d08bf033034"

DEPENDS = "nodejs-native"

SRCREV = "70858644aea11a82855dde816f9cc4f07f5f97a5"
SRC_URI = "git://github.com/enableiot/iotkit-agent.git;protocol=https;branch=master"

S = "${WORKDIR}/git"

do_compile () {
    npm install --production --no-scripts
}

do_install () {
    npm install --production -g --arch=${TARGET_ARCH} --prefix ${D}/usr

    install -d ${D}${sysconfdir}/iotkit-agent/
    install -m 0644 ${S}/config/config.json ${D}${sysconfdir}/iotkit-agent/

    install -d ${D}${systemd_unitdir}/system/
    install -m 0644 ${S}/iotkit-agent.service ${D}${systemd_unitdir}/system/

    install -d ${D}${datadir}/iotkit-agent/
    cp -a ${S}/certs ${D}${datadir}/iotkit-agent/
}

# since the agent requires registration before running we don't want to start
# the systemd service by default

#inherit systemd

#SYSTEMD_SERVICE_${PN} = "iotkit-agent.service"

FILES_${PN} = "${libdir}/node_modules/ \
               ${bindir}/iotkit-admin \
               ${bindir}/iotkit-agent \
               ${datadir}/iotkit-agent/ \
               ${sysconfdir}/iotkit-agent/ \
               ${systemd_unitdir}/system/iotkit-agent.service"

PACKAGES = "${PN}"
