require recipes-graphics/xorg-driver/xorg-driver-video.inc

SUMMARY = "X.Org X server -- Matrox MGA display driver"

DESCRIPTION = "mga is an Xorg driver for Matrox video cards"

LIC_FILES_CHKSUM = "file://COPYING;md5=bc1395d2cd32dfc5d6c57d2d8f83d3fc"

DEPENDS += "virtual/libx11 libxvmc drm xf86driproto glproto \
	    virtual/libgl xineramaproto libpciaccess"

EXTRA_OECONF += "--enable-dri"

PR = "r0"

COMPATIBLE_HOST = '(i.86.*-linux|x86_64.*-linux)'

SRC_URI[md5sum] = "f967fb3e655f6f68aa3f495eaadcaac2"
SRC_URI[sha256sum] = "b657bd5fec4aade6396c683886739b7c8ce57924278bee0e36f13a966eeddff6"
