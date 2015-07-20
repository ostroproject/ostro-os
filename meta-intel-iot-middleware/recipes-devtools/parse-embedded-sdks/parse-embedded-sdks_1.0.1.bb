# Copyright (C) 2015 Brendan Le Foll <brendan.le.foll@intel.com>
# Released under the MIT license (see COPYING.MIT for the terms)

DESCRIPTION = "Lets you use Parse for building Internet of Things (IoT) applications with connected devices"
HOMEPAGE = "https://github.com/ParsePlatform/parse-embedded-sdks"
LICENSE = "Parse License"
LIC_FILES_CHKSUM = "file://LICENSE;md5=340c4660f360f3d393d95ed8c6dd2b28"
SECTION = "libs"
DEPENDS = "curl util-linux"

S = "${WORKDIR}/git"

SRC_URI = "git://github.com/ParsePlatform/parse-embedded-sdks.git;protocol=git;rev=8b4bfd35f1150495e913eab63302265ff28fbb66"

inherit autotools-brokensep
