DESCRIPTION = "6lowpan over 802.15.4 for cc2520 chip on Minnow-Max"

LICENSE = "GPLv2"
LIC_FILES_CHKSUM = "file://${THISDIR}/files/COPYING;md5=12f884d2ae1ff87c09e5b7ccc2c4ca7e"
PR = "r0"

inherit module

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

SRC_URI = "file://spi-minnow-cc2520.c \
           file://Makefile \
           "

S = "${WORKDIR}"
