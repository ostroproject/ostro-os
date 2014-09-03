DESCRIPTION = "Provides communication to the Intel XDK"
HOMEPAGE = "http://somexdkhomepage"
LICENSE = "Propietary"

LIC_FILES_CHKSUM = "file://LICENSE;md5=8a05f85865f8c4b9ba29798e539f93b7"

DEPENDS = "nodejs-native avahi"
RDEPENDS_${PN} = "libarchive-bin"

# URI should point to some external http:// server
SRC_URI = "file://xdk-daemon-${PV}.tar.bz2"
SRC_URI[md5] = "f0ed4083482f1fd54b8b6688c20f8f84"
SRC_URI[sha256] = "c73aa65221da35675d4bdde7e190bfe4d6e376a7468bd87a766bf9c1f5f69ffb"

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
