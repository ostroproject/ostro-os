SUMMARY = "Low Level Skeleton Library for Communication on Intel platforms"
SECTION = "libs"
AUTHOR = "Brendan Le Foll, Tom Ingleby, Yevgeniy Kiveisha"

LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://COPYING;md5=e8db6501ed294e65418a933925d12058"

DEPENDS = "nodejs swig-native maa"

SRC_URI = "git://github.com/intel-iot-devkit/upm.git;protocol=git;rev=b291f372d77e0c65960e9b7e818dca95c5f3af2b"

S = "${WORKDIR}/git"

inherit distutils-base pkgconfig python-dir cmake

FILES_${PN}-doc += "${datadir}/upm/examples/"
