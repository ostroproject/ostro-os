SUMMARY = "The Python interface to the Redis key-value store"
SECTION = "devel/python"
HOMEPAGE = "https://github.com/andymccurdy/redis-py"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE;md5=51d9ad56299ab60ba7be65a621004f27"

SRC_URI = "https://pypi.python.org/packages/source/r/redis/redis-2.10.3.tar.gz"
SRC_URI[md5sum] = "7619221ad0cbd124a5687458ea3f5289"
SRC_URI[sha256sum] = "a4fb37b02860f6b1617f6469487471fd086dd2d38bbce640c2055862b9c4019c"
S = "${WORKDIR}/redis-${PV}"

inherit setuptools
