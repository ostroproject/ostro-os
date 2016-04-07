DESCRIPTION = "6lowpan over 802.15.4 for 802.15.4 chip on Galileo"

LICENSE = "GPLv2"
LIC_FILES_CHKSUM = "file://${THISDIR}/files/COPYING;md5=12f884d2ae1ff87c09e5b7ccc2c4ca7e"
PR = "r0"

# The module is compatible with intel-quark/Galileo Gen2 only
COMPATIBLE_MACHINE="intel-quark"

inherit module

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

RRECOMMENDS_${PN} = "ostro-6lowpan"

SRC_URI = "file://spi-quark-at86rf230.c \
           file://spi-quark-board.c \
           file://spi-quark-board.h \
           file://Makefile \
           file://modules-load.d/at86rf230.conf.sample \
           "

FILES_${PN} += " /usr/lib/modules-load.d/at86rf230.conf.sample \
               "
# Sample configuring file
do_install_append () {
	install -d -m 755 ${D}${libdir}/modules-load.d
	install -m 0644 modules-load.d/at86rf230.conf.sample ${D}${libdir}/modules-load.d/
}

S = "${WORKDIR}"
