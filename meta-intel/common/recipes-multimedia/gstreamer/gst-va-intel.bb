DESCRIPTION = "Video Acceleration Add-ons for Intel BSPs"
LICENSE = "MIT"
DEPENDS = "gst-meta-base"
LIC_FILES_CHKSUM = "file://${COREBASE}/LICENSE;md5=3f40d7994397109285ec7b81fdeb3b58 \
                    file://${COREBASE}/meta/COPYING.MIT;md5=3da9cfbcb788c80a0384361b4de20420"

PR = "r0"

PACKAGES = "\
    gst-va-intel \
    gst-va-intel-general \
    gst-va-intel-video \
    "

ALLOW_EMPTY = "1"

RDEPENDS_gst-va-intel = "\
    gst-va-intel-general \
    gst-va-intel-video \
    "

RDEPENDS_gst-va-intel-general = "\
    gst-ffmpeg \
    "

RDEPENDS_gst-va-intel-video = "\
    gst-plugins-good-isomp4 \
    "
