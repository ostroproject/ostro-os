DESCRIPTION = "Wylodrin is something..."
HOMEPAGE = "http://github.com/Wyliodrin/wyliodrin-server-nodejs"
LICENSE = "GPLv2"

LIC_FILES_CHKSUM = "file://LICENSE;md5=ee16d9b084e359d55ef7cd1ac439f6ba"

DEPENDS = "nodejs-native fuse icu"
RDEPENDS_${PN} = "libwyliodrin"

SRC_URI = "git://github.com/Wyliodrin/wyliodrin-server-nodejs.git;branch=development;protocol=git;rev=14ccfd779997dddec3e381515e0f5b22a9862e96 \
           file://wyliodrin-server.service \
           file://redis.service"

S = "${WORKDIR}/git"

# we don't care about debug for the few binary node modules
INHIBIT_PACKAGE_DEBUG_SPLIT = "1"
INSANE_SKIP_${PN} = "staticdev"

do_compile () {
    npm install --ignore-scripts --arch=${TARGET_ARCH}
}

do_install () {
    export LD="${CXX}"
    npm install -g --arch=${TARGET_ARCH} --prefix ${D}/usr/
    echo -n "arduinogalileo" > ${D}${libdir}/node_modules/${PN}/board.type
    cp patch/index.js ${D}${libdir}/node_modules/${PN}/node_modules/node-xmpp-client/
    cp patch/session.js ${D}${libdir}/node_modules/${PN}/node_modules/node-xmpp-client/lib/
    cp patch/websockets.js ${D}${libdir}/node_modules/${PN}/node_modules/node-xmpp-client/lib/
    install -d ${D}${systemd_unitdir}/system/
    install -m 0644 ${WORKDIR}/redis.service ${D}${systemd_unitdir}/system/
    install -m 0644 ${WORKDIR}/wyliodrin-server.service ${D}${systemd_unitdir}/system/
}

FILES_${PN} = "${bindir}/wyliodrin-server-nodejs \
               ${libdir}/node_modules/wyliodrin-server-nodejs/ \
               ${systemd_unitdir}/system/wylodrin-server.service \
               ${systemd_unitdir}/system/redis.service"

PACKAGES = "${PN}"

inherit systemd

SYSTEMD_SERVICE_${PN} = "redis.service \
                         wyliodrin-server.service"
