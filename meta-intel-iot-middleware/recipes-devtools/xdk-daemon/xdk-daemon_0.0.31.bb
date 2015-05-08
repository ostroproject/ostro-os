DESCRIPTION = "Provides communication to the Intel XDK"
LICENSE = "Proprietary"

LIC_FILES_CHKSUM = "file://LICENSE;md5=121fc3cd97e5c1db39627399a7d72288"

DEPENDS = "nodejs-native mdns"
RDEPENDS_${PN} = "libarchive-bin mdns nodejs"

PR = "r0"

# needed to unset no_proxy for internal development
export no_proxy = ""

SRC_URI = "http://download.xdk.intel.com/iot/xdk-daemon-0.0.31.tar.bz2"
SRC_URI[md5sum] = "3c0cd1d643e880358c805798eaa69e9e"
SRC_URI[sha256sum] = "1117680926a3cbcdd6254edc2b74af4d0d28c78875c6acf604b1881783405c3c"

# we don't care about debug for the few binary node modules
INHIBIT_PACKAGE_DEBUG_SPLIT = "1"

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

    npm install --arch=${TARGET_ARCH}
    cd current/ && npm install --arch=${TARGET_ARCH}
    cd node-inspector-server && npm install --arch=${TARGET_ARCH}

    sed -i '/TM/d' ${S}/xdk-daemon
}

do_install () {
    install -d ${D}/opt/xdk-daemon/
    cp -a ${S}/* ${D}/opt/xdk-daemon/

    install -d ${D}${systemd_unitdir}/system/
    install -m 0644 ${S}/xdk-daemon-mdns.service ${D}${systemd_unitdir}/system/xdk-daemon.service

    install -d ${D}${bindir}
    ln -s /opt/xdk-daemon/current/xdk-whitelist ${D}${bindir}/xdk-whitelist
}

inherit systemd

SYSTEMD_SERVICE_${PN} = "xdk-daemon.service"

FILES_${PN} = "/opt/xdk-daemon/ \
               ${systemd_unitdir}/system/xdk-daemon.service \
               ${bindir}/"

PACKAGES = "${PN}"
