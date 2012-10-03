DESCRIPTION = "GStreamer Video Acceleration Add-ons for Intel BSPs"
LICENSE = "MIT"
DEPENDS = "gst-meta-base"
LIC_FILES_CHKSUM = "file://${COREBASE}/LICENSE;md5=3f40d7994397109285ec7b81fdeb3b58 \
                    file://${COREBASE}/meta/COPYING.MIT;md5=3da9cfbcb788c80a0384361b4de20420"

PR = "r2"

def map_gst_vaapi(d):
    if base_contains('MACHINE_FEATURES', 'va-impl-mixvideo', "1", "0", d) == "1":
       return "gst-va-mixvideo-vaapi"
    if base_contains('MACHINE_FEATURES', 'va-impl-intel', "1", "0", d) == "1":
       return "gst-va-intel-vaapi"
    return ""

VAAPI_IMPL = "${@map_gst_vaapi(d)}"

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
    ${@bb.utils.contains("LICENSE_FLAGS_WHITELIST", \
    "commercial", "gst-ffmpeg", "", d)} \
    "

RDEPENDS_gst-va-intel-video = "\
    gst-plugins-good-isomp4 \
    "

# The gstreamer-vaapi package contains the vaapi implementation
#
RDEPENDS_gst-va-intel-vaapi = "\
    gstreamer-vaapi \
    "

# The emgd driver contains the vaapi implementation
#
RDEPENDS_gst-va-mixvideo-vaapi = "\
    emgd-driver-bin \
    "
