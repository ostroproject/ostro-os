SUMMARY = "C library and program for reading the TEMPer family of thermometer and hygrometer devices"
SECTION = "libs"
AUTHOR = "Frode Austvik"
HOMEPAGE = "https://github.com/edorfaus/TEMPered"

LICENSE = "BSD-2-Clause"

LIC_FILES_CHKSUM = "file://LICENSE;md5=7a3b4938b14feadc92e125c3af60e69a"

DEPENDS = "hid-api"

SRC_URI = "git://github.com/edorfaus/TEMPered.git;protocol=git;rev=e77ee06305e3252e58d9a35d0b06a99b3888c0df \
           file://0001-common.c-remove-duplicate-declarations-of-int-i.patch"

S = "${WORKDIR}/git"

inherit distutils-base pkgconfig cmake
