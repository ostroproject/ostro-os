DESCRIPTION = "6lowpan over 802.15.4 for 802.15.4 chip on Minnow-Max"

LICENSE = "GPLv2"
LIC_FILES_CHKSUM = "file://${THISDIR}/files/COPYING;md5=12f884d2ae1ff87c09e5b7ccc2c4ca7e"
PR = "r0"

inherit module

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

SRC_URI = "file://spi-minnow-cc2520.c \
           file://spi-minnow-at86rf230.c \
           file://spi-minnow-board.c \
           file://spi-minnow-board.h \
           file://Makefile \
           "

S = "${WORKDIR}"
