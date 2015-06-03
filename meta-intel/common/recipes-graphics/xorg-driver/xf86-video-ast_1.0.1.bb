require recipes-graphics/xorg-driver/xorg-driver-video.inc

SUMMARY = "X.Org X server -- ASpeed Technologies graphics driver"

DESCRIPTION = "ast is an Xorg driver for ASpeed Technologies video cards"

LIC_FILES_CHKSUM = "file://COPYING;md5=0b8c242f0218eea5caa949b7910a774b"

DEPENDS += "libpciaccess"

SRC_URI[md5sum] = "63ac98d6526e3e27e290e1836a229059"
SRC_URI[sha256sum] = "e778f1824f5eed7e3197f00f39418de1525e310fd78e0335f6178c26b9b0495b"
