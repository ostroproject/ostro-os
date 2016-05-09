DESCRIPTION = "Analog Devices Libiio"
DEPENDS = "libxml2 bison flex avahi"
LICENSE = "LGPLv2.1"
LIC_FILES_CHKSUM = "file://COPYING.txt;md5=7c13b3376cea0ce68d2d2da0a1b3a72c"
PV = "0.6"

SRC_URI = "git://github.com/analogdevicesinc/libiio.git;protocol=git;"

SRCREV = "cfd88fd09281c07992348118895998ca0e598847"

S = "${WORKDIR}/git"

inherit autotools cmake

