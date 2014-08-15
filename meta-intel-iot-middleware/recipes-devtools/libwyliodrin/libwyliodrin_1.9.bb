DESCRIPTION = "helper library for wyliodrin nodejs server"
HOMEPAGE = "http://github.com/Wyliodrin/libwyliodrin"
LICENSE = "GPLv2"
SECTION = "libs"
DEPENDS = "icu fuse mraa hiredis jansson swig-native"
PR = "r0"

LIC_FILES_CHKSUM = "file://LICENSE;md5=e8c1458438ead3c34974bc0be3a03ed6"

SRC_URI = "git://github.com/Wyliodrin/libwyliodrin.git;protocol=git;rev=aeaa2d2da18d97e7db9d080095d2cfc323b30183 \
           file://0001-SeeedOLED.h-fix-Wire.h-include.patch"

S = "${WORKDIR}/git"

inherit distutils-base pkgconfig python-dir cmake

EXTRA_OECMAKE="-DGALILEO=ON"
