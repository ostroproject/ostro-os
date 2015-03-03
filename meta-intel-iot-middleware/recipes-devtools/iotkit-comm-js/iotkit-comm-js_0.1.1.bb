DESCRIPTION = "Inter of Things communication library for device-to-device and device-to-cloud messaging"
LICENSE = "MIT"

PR = "r2"

SRC_URI = "git://github.com/intel-iot-devkit/iotkit-comm-js.git;protocol=https"
SRCREV = "3d78d3cf097dfbbb5a9f554497dec5ba8456a35c"

LIC_FILES_CHKSUM = " \
        file://COPYING;md5=e8db6501ed294e65418a933925d12058 \
"

S = "${WORKDIR}/git"

DEPENDS = "nodejs-native zeromq mdns paho-mqtt iotkit-lib-c"

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
    npm --arch=${TARGET_ARCH} --verbose install
}

do_install () {
    install -d ${D}${libdir}/node_modules/iotkit-comm/
    cp -r ${S}/node_modules ${D}${libdir}/node_modules/iotkit-comm/
    install -m 644 ${S}/package.json ${D}${libdir}/node_modules/iotkit-comm/
    install -m 644 ${S}/COPYING ${D}${libdir}/node_modules/iotkit-comm/
    install -m 644 ${S}/README.md ${D}${libdir}/node_modules/iotkit-comm/
    install -m 644 ${S}/jsdoc-conf.json ${D}${libdir}/node_modules/iotkit-comm/
    cp -r ${S}/lib ${D}${libdir}/node_modules/iotkit-comm/
    cp -r ${S}/test ${D}${libdir}/node_modules/iotkit-comm/
    cp -r ${S}/doc ${D}${libdir}/node_modules/iotkit-comm/
    install -d ${D}${datadir}/iotkit-comm/examples/node
    cp -r ${S}/example/* ${D}${datadir}/iotkit-comm/examples/node

    chmod 755 ${D}${libdir}/node_modules/iotkit-comm/lib/setup.js
    install -d ${D}${bindir}
    ln -s ../lib/node_modules/iotkit-comm/lib/setup.js ${D}${bindir}/iotkit-comm
}

INHIBIT_PACKAGE_STRIP = "1"

PACKAGES = "${PN} ${PN}-test-dependencies"

FILES_${PN}-test-dependencies = " \
        ${libdir}/node_modules/iotkit-comm/node_modules/.bin/istanbul \
        ${libdir}/node_modules/iotkit-comm/node_modules/.bin/jsdoc \
        ${libdir}/node_modules/iotkit-comm/node_modules/.bin/mocha \
        ${libdir}/node_modules/iotkit-comm/node_modules/.bin/_mocha \
        ${libdir}/node_modules/iotkit-comm/node_modules/chai/ \
        ${libdir}/node_modules/iotkit-comm/node_modules/istanbul/ \
        ${libdir}/node_modules/iotkit-comm/node_modules/jsdoc/ \
        ${libdir}/node_modules/iotkit-comm/node_modules/mocha/ \
"

FILES_${PN} = " \
        ${libdir}/node_modules/iotkit-comm/doc/ \
        ${libdir}/node_modules/iotkit-comm/jsdoc-conf.json \
        ${libdir}/node_modules/iotkit-comm/COPYING \
        ${libdir}/node_modules/iotkit-comm/lib/ \
        ${libdir}/node_modules/iotkit-comm/package.json \
        ${libdir}/node_modules/iotkit-comm/README.md \
        ${libdir}/node_modules/iotkit-comm/test \
        ${libdir}/node_modules/iotkit-comm/node_modules/.bin/mqtt_pub \
        ${libdir}/node_modules/iotkit-comm/node_modules/.bin/mqtt_sub \
        ${libdir}/node_modules/iotkit-comm/node_modules/async/ \
        ${libdir}/node_modules/iotkit-comm/node_modules/commander/ \
        ${libdir}/node_modules/iotkit-comm/node_modules/mdns2/ \
        ${libdir}/node_modules/iotkit-comm/node_modules/mqtt/ \
        ${libdir}/node_modules/iotkit-comm/node_modules/read/ \
        ${libdir}/node_modules/iotkit-comm/node_modules/zmq/ \
        ${datadir}/iotkit-comm/examples/ \
        ${bindir}/iotkit-comm \
"

RDEPENDS_${PN} = "nodejs zeromq mdns paho-mqtt mosquitto sshpass iotkit-lib-c"
RDEPENDS_${PN}-test-dependencies = "${PN}"
