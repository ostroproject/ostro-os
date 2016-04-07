DESCRIPTION = "6lowpan over 802.15.4 for 802.15.4 chip on Minnow-Max"

LICENSE = "GPLv2"
LIC_FILES_CHKSUM = "file://${THISDIR}/files/COPYING;md5=12f884d2ae1ff87c09e5b7ccc2c4ca7e"
PR = "r0"

# The module is compatible with intel-corei7-64/Minnowboard only
COMPATIBLE_MACHINE="intel-corei7-64"

inherit module

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

RRECOMMENDS_${PN} = "ostro-6lowpan"

SRC_URI = "file://spi-minnow-cc2520.c \
           file://spi-minnow-at86rf230.c \
           file://spi-minnow-board.c \
           file://spi-minnow-board.h \
           file://Makefile \
           file://modules-load.d/cc2520.conf.sample \
           file://modprobe.d/spi-minnow-cc2520.conf.sample \
           file://modules-load.d/at86rf230.conf.sample \
           file://modprobe.d/spi-minnow-at86rf230.conf.sample \
           "

FILES_${PN} += " /usr/lib/modules-load.d/cc2520.conf.sample \
                 /usr/lib/modules-load.d/at86rf230.conf.sample \
                 /lib/modprobe.d/spi-minnow-cc2520.conf.sample \
                 /lib/modprobe.d/spi-minnow-at86rf230.conf.sample \
               "

# Sample configuring file
do_install_append () {
	install -d -m 755 ${D}${base_libdir}/modprobe.d
	install -d -m 755 ${D}${libdir}/modules-load.d
	install -m 0644 modules-load.d/cc2520.conf.sample ${D}${libdir}/modules-load.d/
	install -m 0644 modprobe.d/spi-minnow-cc2520.conf.sample ${D}${base_libdir}/modprobe.d/
	install -m 0644 modules-load.d/at86rf230.conf.sample ${D}${libdir}/modules-load.d/
	install -m 0644 modprobe.d/spi-minnow-at86rf230.conf.sample ${D}${base_libdir}/modprobe.d/
}

S = "${WORKDIR}"
