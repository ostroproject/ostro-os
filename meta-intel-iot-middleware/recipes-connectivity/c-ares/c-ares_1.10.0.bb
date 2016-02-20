DESCRIPTION = "C library for asynchronous DNS requests (including name resolves)"
HOMEPAGE = "http://c-ares.haxx.se/"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://README;beginline=17;endline=23;md5=d08205a43bc63c12cf394ac1d2cce7c3"

PR = "r0"

SRC_URI = "http://c-ares.haxx.se/download/c-ares-${PV}.tar.gz"

SRC_URI[md5sum] = "1196067641411a75d3cbebe074fd36d8"
SRC_URI[sha256sum] = "3d701674615d1158e56a59aaede7891f2dde3da0f46a6d3c684e0ae70f52d3db"

inherit autotools
