require recipes-graphics/xorg-driver/xorg-driver-video.inc

SUMMARY = "X.Org X server -- ASpeed Technologies graphics driver"

DESCRIPTION = "ast is an Xorg driver for ASpeed Technologies video cards"

LIC_FILES_CHKSUM = "file://COPYING;md5=0b8c242f0218eea5caa949b7910a774b"

DEPENDS += "libpciaccess"

SRC_URI[md5sum] = "c3f15602db18e91842245a43a297cc42"
SRC_URI[sha256sum] = "90225bc4832da9cd11e3130f0c210ed67f4f48a4ce35f1bb83bd5cc0c7d916a1"
