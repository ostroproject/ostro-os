DESCRIPTION = "Wylodrin is something..."
HOMEPAGE = "http://github.com/alexandruradovici/wyliodrin-server/tree/clean"
LICENSE = "GPLv2"

LIC_FILES_CHKSUM = "file://README.md;md5=9103f988484919725abe920c4cd2d021"

DEPENDS = "jansson fuse libevent libstrophe hiredis curl"
RDEPENDS_${PN} = "libwyliodrin redis"

SRC_URI = "git://github.com/alexandruradovici/wyliodrin-server;branch=clean;protocol=git;rev=826957e380f886f5694dc00011feae09604ccbe7 \
           file://wyliodrin-server.service"

S = "${WORKDIR}/git"

inherit cmake systemd

PARALLEL_MAKE=""

SYSTEMD_SERVICE_${PN} = "wyliodrin-server.service"

do_install_append () {
    install -d ${D}${systemd_unitdir}/system/
    install -m 0644 ${WORKDIR}/wyliodrin-server.service ${D}${systemd_unitdir}/system/
}

