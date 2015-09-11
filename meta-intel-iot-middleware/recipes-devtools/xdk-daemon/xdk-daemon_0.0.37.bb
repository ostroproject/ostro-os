DESCRIPTION = "Provides communication to the Intel XDK"
LICENSE = "Proprietary"

LIC_FILES_CHKSUM = "file://LICENSE;md5=121fc3cd97e5c1db39627399a7d72288"

DEPENDS = "nodejs-native mdns"
RDEPENDS_${PN} = "libarchive-bin nodejs bash"

PR = "r0"

# needed to unset no_proxy for internal development
export no_proxy = ""

SRC_URI = "http://download.xdk.intel.com/iot/xdk-daemon-0.0.37.tar.bz2"
SRC_URI[md5sum] = "8ecc2d2c931d82bb5aaaeb2afefeee06"
SRC_URI[sha256sum] = "624e534b5620db59105e3014278aebc5ef4da855be218dc1006351ab9c8a08dd"

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

    # NPM is picky about arch names
    if [ "${TARGET_ARCH}" == "i586" ]; then
        npm config set target_arch ia32
        export TARGET_ARCH=ia32
    fi
    # npm is dumb, it needs to get given --arch but not in npm config
    npm install
    cd current/ && npm install --arch=${TARGET_ARCH}
    cd node-inspector-server && npm install --build-from-source --arch=${TARGET_ARCH}

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
