DESCRIPTION = "helper library for wyliodrin nodejs server"
HOMEPAGE = "http://github.com/Wyliodrin/libwyliodrin"
LICENSE = "GPLv2"
SECTION = "libs"
DEPENDS = "icu fuse mraa hiredis jansson swig-native"
RDEPENDS_${PN} = "python-redis bash"
PR = "r0"

LIC_FILES_CHKSUM = "file://LICENSE;md5=e8c1458438ead3c34974bc0be3a03ed6"

SRC_URI = "git://github.com/Wyliodrin/libwyliodrin.git;protocol=git;rev=c5eeecadf75d632fb5d1b0a87e6a51b21d533c4b"

S = "${WORKDIR}/git"

inherit distutils-base pkgconfig python-dir cmake

EXTRA_OECMAKE="-DGALILEO=ON"
