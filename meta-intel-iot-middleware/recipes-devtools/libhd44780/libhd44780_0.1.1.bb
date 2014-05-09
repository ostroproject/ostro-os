DESCRIPTION = "LCD library that communicates with a HD44780 LCD (saintsmart LCD2004) on i2c"
HOMEPAGE = "http://developer.intel.com/"
SECTION = "utils"

LICENSE = "MIT & GPLv2 & LGPLv2.1"
LIC_FILES_CHKSUM = "file://COPYING;md5=e8db6501ed294e65418a933925d12058"

SRC_URI = "file://libhd44780-0.1.1.tar.bz2 \
           file://libs.patch"

SRC_URI[md5sum] = "b2a37446979d91d3fbea9d436f2f0f2b"
SRC_URI[sha256] = "40fa44a0fa250ba9a1882b0cf194b5c849b331792218daeba298785e4a7b632b"

inherit cmake
