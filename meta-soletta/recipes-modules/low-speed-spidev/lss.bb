#
# Yocto recipe to build a kernel module out of the kernel tree
# lss.bb
#

DESCRIPTION = "Low Speed Spidev"
SECTION = "modules"
LICENSE = "GPLv2"
LIC_FILES_CHKSUM = "file://COPYING;md5=12f884d2ae1ff87c09e5b7ccc2c4ca7e"
PR = "r0"

inherit module

SRC_URI =   "file://low-speed-spidev.c \
            file://Makefile \
            file://COPYING \
            file://low-speed-spidev.conf \
            "

FILES_${PN} += "/etc/modprobe.d/low-speed-spidev.conf"

# Configuring to start on boot low-speed-spidev
do_install_append () {
  install -m 0655 low-speed-spidev.conf ${D}/etc/modprobe.d/
}

S = "${WORKDIR}"
