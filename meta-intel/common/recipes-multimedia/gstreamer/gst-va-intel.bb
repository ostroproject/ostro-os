DESCRIPTION = "GStreamer Video Acceleration Add-ons for Intel BSPs"
LICENSE = "MIT"
DEPENDS = "gst-meta-base"
LIC_FILES_CHKSUM = "file://${COREBASE}/LICENSE;md5=3f40d7994397109285ec7b81fdeb3b58 \
                    file://${COREBASE}/meta/COPYING.MIT;md5=3da9cfbcb788c80a0384361b4de20420"

PR = "r0"

VAAPI_IMPL = "${@base_contains('MACHINE_FEATURES', 'gst-va-mixvideo', 'gst-va-mixvideo-vaapi', \
             'gst-va-intel-vaapi', d)}"

PACKAGES = "\
    gst-va-intel \
    gst-va-intel-general \
    gst-va-intel-video \
    ${VAAPI_IMPL} \
    "

ALLOW_EMPTY = "1"

RDEPENDS_gst-va-intel = "\
    gst-va-intel-general \
    gst-va-intel-video \
    ${VAAPI_IMPL} \
    "

RDEPENDS_gst-va-intel-general = "\
    gst-ffmpeg \
    "

RDEPENDS_gst-va-intel-video = "\
    gst-plugins-good-isomp4 \
    "

RDEPENDS_gst-va-intel-vaapi = "\
    gstreamer-vaapi \
    "

RDEPENDS_gst-va-mixvideo-vaapi = "\
    emgd-driver-bin \
    "
