DESCRIPTION = "helper library for wyliodrin nodejs server"
HOMEPAGE = "http://github.com/Wyliodrin/libwyliodrin"
LICENSE = "GPLv2"
SECTION = "libs"
DEPENDS = "icu fuse mraa hiredis jansson swig-native"
RDEPENDS_${PN} = "python-redis bash"
PR = "r0"

LIC_FILES_CHKSUM = "file://LICENSE;md5=e8c1458438ead3c34974bc0be3a03ed6"

SRC_URI = "git://github.com/Wyliodrin/libwyliodrin.git;protocol=git;rev=7ea3b5344d683b93240d40ef03959632279b1cac \
           file://0001-LiquidCrystal.cpp-inline-functions-need-to-be-inline.patch"

S = "${WORKDIR}/git"

inherit distutils-base pkgconfig python-dir cmake

EXTRA_OECMAKE="-DGALILEO=ON"
