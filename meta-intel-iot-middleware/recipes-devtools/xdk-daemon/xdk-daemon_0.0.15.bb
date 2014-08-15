DESCRIPTION = "Provides communication to the Intel XDK"
HOMEPAGE = "http://somexdkhomepage"
LICENSE = "Propietary"

LIC_FILES_CHKSUM = "file://LICENSE;md5=177a04615d21d7547ea0af81fda69dae"

DEPENDS = "nodejs-native avahi"
RDEPENDS_${PN} = "libarchive-bin"

# URI should point to some external http:// server
SRC_URI = "file://xdk-daemon-${PV}.tar.bz2"
SRC_URI[md5] = "02f13d5ed715ac4417e6fa25ba2890db"
SRC_URI[sha256] = "ee8925d2116e7dc06b3b9a9ac72f247d87bee53abccf395da853a35087660304"

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
