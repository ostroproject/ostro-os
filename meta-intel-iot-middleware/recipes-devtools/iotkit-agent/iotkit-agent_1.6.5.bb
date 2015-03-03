DESCRIPTION = "Transparently implements the necessary message formats and transport security as well as device registration"
HOMEPAGE = "http://enableiot.com"
LICENSE = "BSD-2-Clause & BSD-3-Clause & GPL-2.0 & Apache-2.0 & MIT & PD"

LIC_FILES_CHKSUM = "file://${WORKDIR}/git/LICENSE;md5=30c8ae0368f724cf5f753d08bf033034"

DEPENDS = "nodejs-native"

SRC_URI = "git://github.com/enableiot/iotkit-agent.git;protocol=git"
SRCREV = "47c3ab71d22088a951abf120715e9ec5755b7fa0"

S = "${WORKDIR}/git"

do_compile () {
    # changing the home directory to the working directory, the .npmrc will be created in this directory
    export HOME=${WORKDIR}

    # does not build dev packages
    npm config set dev false

    # access npm registry using http
    npm set strict-ssl false
    npm config set registry http://registry.npmjs.org/

    # configure http proxy if neccessary
    if [ -n "${http_proxy}" ]; then
        npm config set proxy ${http_proxy}
    fi
    if [ -n "${HTTP_PROXY}" ]; then
        npm config set proxy ${HTTP_PROXY}
    fi

    # configure cache to be in working directory
    npm set cache ${WORKDIR}/npm_cache

    # clear local cache prior to each compile
    npm cache clear

    # compile and install  node modules in source directory
    npm --arch=${TARGET_ARCH} --production --verbose install
}

do_install () {
    install -d ${D}${libdir}/node_modules/iotkit-agent/
    cp -r ${S}/* ${D}${libdir}/node_modules/iotkit-agent/
    rm -rf ${D}${libdir}/node_modules/iotkit-agent/buildscripts

    install -d ${D}${bindir}
    ln -s ../lib/node_modules/iotkit-agent/iotkit-agent.js ${D}${bindir}/iotkit-agent
    ln -s ../lib/node_modules/iotkit-agent/iotkit-admin.js ${D}${bindir}/iotkit-admin

    install -d ${D}${systemd_unitdir}/system/
    install -m 0644 ${S}/iotkit-agent.service ${D}${systemd_unitdir}/system/
}

inherit systemd

# since the agent requires registration before running we don't want to start
# the systemd service by default
SYSTEMD_AUTO_ENABLE = "disable"
SYSTEMD_SERVICE_${PN} = "iotkit-agent.service"

FILES_${PN} = "${libdir}/node_modules/ \
               ${bindir}/ \
"

PACKAGES = "${PN}"
