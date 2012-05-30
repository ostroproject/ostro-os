SUMMARY = "VA-API support to GStreamer"
DESCRIPTION = "gstreamer-vaapi consists of a collection of VA-API \
based plugins for GStreamer and helper libraries: `vaapidecode', \
`vaapiconvert', and `vaapisink'."

LICENSE = "LGPLv2.1+"
LIC_FILES_CHKSUM = "file://COPYING.LIB;md5=4fbd65380cdd255951079008b364516c"

DEPENDS = "gstreamer libva ffmpeg"

# 0.2.9 tag
SRCREV = "c98c14bd32855467a5a0ff21b6c703e9e3461467"
PV = "0.2.9+git${SRCPV}"
PR = "r0"

SRC_URI = "git://gitorious.org/vaapi/gstreamer-vaapi.git \
           file://glib-includes.patch"

SRC_URI[md5sum] = "729d75f21df79114a8c81d896489e5ad"
SRC_URI[sha256sum] = "f1770c4537f1615701dbc845eee5732fbb1036b3acafbc7488e551fab334a31d"

S = "${WORKDIR}/git"

inherit autotools pkgconfig gtk-doc

FILES_${PN} += "${libdir}/gstreamer-0.10/*.so"
FILES_${PN}-dbg += "${libdir}/gstreamer-0.10/.debug"
FILES_${PN}-dev += "${libdir}/gstreamer-0.10/*.la ${libdir}/gstreamer-0.10/*.a"
