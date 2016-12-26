SUMMARY = "Yami is media infrastructure base on libva"
DESCRIPTION = "Yet Another Media Infrastructure \
light weight hardware codec library base on VA-API "

HOMEPAGE = "https://github.com/01org/libyami"
BUGTRACKER = "https://github.com/01org/libyami/issues/new"

LICENSE = "Apache-2.0"
SRC_URI = "https://github.com/01org/libyami/archive/libyami-${PV}.tar.gz"

LIC_FILES_CHKSUM = "file://COPYING.LIB;md5=3b83ef96387f14655fc854ddc3c6bd57"

SRC_URI[md5sum] = "666909504c693f4b9186237b86ba43dc"
SRC_URI[sha256sum] = "1051d3e3366a933c4fbfb883b3900e81a8c0e4e1cd4d5a08b9c7d4e1bf7cec34"

S = "${WORKDIR}/libyami-libyami-${PV}"

PACKAGECONFIG ??= "${@bb.utils.contains("DISTRO_FEATURES", "x11", "x11", "", d)}"
PACKAGECONFIG[x11] = "--enable-x11,--disable-x11,virtual/libx11 libxrandr libxrender"

DEPENDS = "libva"
inherit autotools pkgconfig
