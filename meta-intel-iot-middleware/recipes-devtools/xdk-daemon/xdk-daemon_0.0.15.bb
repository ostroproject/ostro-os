DESCRIPTION = "Provides communication to the Intel XDK"
HOMEPAGE = "http://somexdkhomepage"
LICENSE = "Propietary"

LIC_FILES_CHKSUM = "file://LICENSE;md5=37df31ee5c72616fa8d911395a1449c5"

DEPENDS = "nodejs-native avahi"
RDEPENDS_${PN} = "libarchive-bin"

# URI should point to some external http:// server
SRC_URI = "file://xdk-daemon-${PV}.tar.bz2"
SRC_URI[md5] = "1345a5ae88fd3b0bf11dd623063283b7"
SRC_URI[sha256] = "ea9277188dab049e3eb11470f8c0c2fefebedb941ec3a204a8ff41f8e64b76b6"

# we don't care about debug for the few binary node modules
INHIBIT_PACKAGE_DEBUG_SPLIT = "1"

do_compile () {
    export CPLUS_INCLUDE_PATH=${PKG_CONFIG_SYSROOT_DIR}/usr/include/avahi-compat-libdns_sd
    npm install --arch=${TARGET_ARCH}
    cd current/ && npm install --arch=${TARGET_ARCH}
    cd node-inspector-server && npm install --arch=${TARGET_ARCH}

    # fix bin path for xdk-daemon
    #sed -i 's/appDaemon/xdk-daemon/' ${S}/xdk-daemon.service
    # remove date hack from start script
    sed -i '/TM/d' ${S}/xdk-daemon
}

do_install () {
    install -d ${D}/opt/xdk-daemon/
    cp -a ${S}/* ${D}/opt/xdk-daemon/

    install -d ${D}${systemd_unitdir}/system/
    install -m 0644 ${S}/xdk-daemon.service ${D}${systemd_unitdir}/system/
}

inherit systemd

SYSTEMD_SERVICE_${PN} = "xdk-daemon.service"

FILES_${PN} = "/opt/xdk-daemon/ \
               ${systemd_unitdir}/system/xdk-daemon.service"

PACKAGES = "${PN}"
