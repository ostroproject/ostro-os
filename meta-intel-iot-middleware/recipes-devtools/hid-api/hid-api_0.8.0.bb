SUMMARY = "Low Level HID-API package on Intel platforms"
SECTION = "libs"
AUTHOR = "Alan Ott"
HOMEPAGE = "https://github.com/signal11/hidapi"
LICENSE = "BSD-3-Clause | GPLv3"

LIC_FILES_CHKSUM = "file://LICENSE.txt;md5=7c3949a631240cb6c31c50f3eb696077"

DEPENDS = "libusb udev"

SRC_URI = "git://github.com/signal11/hidapi.git;protocol=git;rev=3a66d4e513ed1b1ce82b7e6fcfa30ff05598b696"

S = "${WORKDIR}/git"

inherit distutils-base pkgconfig autotools

