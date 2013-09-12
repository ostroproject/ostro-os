require recipes-graphics/xorg-driver/xorg-driver-video.inc

SUMMARY = "X.Org X server -- Matrox MGA display driver"

DESCRIPTION = "mga is an Xorg driver for Matrox video cards"

LIC_FILES_CHKSUM = "file://COPYING;md5=bc1395d2cd32dfc5d6c57d2d8f83d3fc"

SRC_URI += "file://checkfile.patch"

DEPENDS += "virtual/libx11 libpciaccess"

PR = "r1"

COMPATIBLE_HOST = '(i.86.*-linux|x86_64.*-linux)'

SRC_URI[md5sum] = "f543877db4e260d8b43c7da3095605ed"
SRC_URI[sha256sum] = "3f89ce250eea93f0de890954687790e06c0bab9e3e303df393e8759a187eca6c"

PACKAGECONFIG ?= "${@base_contains('DISTRO_FEATURES', 'opengl', 'dri', '', d)}"
PACKAGECONFIG[dri] = "--enable-dri,--disable-dri,drm xf86driproto,xserver-xorg-extension-dri"

RDEPENDS_${PN} = "xserver-xorg-module-exa"
