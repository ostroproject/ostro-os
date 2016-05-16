require recipes-graphics/xorg-driver/xorg-driver-video.inc

SUMMARY = "X.Org X server -- Matrox MGA display driver"

DESCRIPTION = "mga is an Xorg driver for Matrox video cards"

LIC_FILES_CHKSUM = "file://COPYING;md5=bc1395d2cd32dfc5d6c57d2d8f83d3fc"

SRC_URI += "file://checkfile.patch"

DEPENDS += "virtual/libx11 libpciaccess"

PR = "r1"

COMPATIBLE_HOST = '(i.86.*-linux|x86_64.*-linux)'

SRC_URI[md5sum] = "cd3db8370caa3e607614ea4e74d4c350"
SRC_URI[sha256sum] = "48c6690b6751c76f53de64f8dbeaa9d6c62dbcfe890c768fd87167951247d44f"

PACKAGECONFIG ?= "${@bb.utils.contains('DISTRO_FEATURES', 'opengl', 'dri', '', d)}"
PACKAGECONFIG[dri] = "--enable-dri,--disable-dri,drm xf86driproto,xserver-xorg-extension-dri"

RDEPENDS_${PN} = "xserver-xorg-module-exa"
