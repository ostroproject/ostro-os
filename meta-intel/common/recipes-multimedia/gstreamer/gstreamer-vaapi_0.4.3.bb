SUMMARY = "VA-API support to GStreamer"
DESCRIPTION = "gstreamer-vaapi consists of a collection of VA-API \
based plugins for GStreamer and helper libraries: `vaapidecode', \
`vaapiconvert', and `vaapisink'."

LICENSE = "LGPLv2.1+"
LIC_FILES_CHKSUM = "file://COPYING.LIB;md5=4fbd65380cdd255951079008b364516c"

DEPENDS = "gstreamer gst-plugins-base gst-plugins-bad libva"

SRC_URI = "http://www.freedesktop.org/software/vaapi/releases/${BPN}/${BPN}-${PV}.tar.bz2"
SRC_URI[md5sum] = "7b1ede7193bc5a0aca921c490684f7b5"
SRC_URI[sha256sum] = "68e0598456fe17085f6b8b1ce3da066322cc02c363955fb319776a5404d2b0da"

inherit autotools pkgconfig gtk-doc

PACKAGECONFIG ??= "${@base_contains("DISTRO_FEATURES", "x11", "x11", "", d)} \
                   ${@base_contains("DISTRO_FEATURES", "wayland", "wayland", "", d)}"
PACKAGECONFIG[x11] = "--enable-x11,--disable-x11,virtual/libx11 libxrandr"
PACKAGECONFIG[wayland] = "--enable-wayland,--disable-wayland,wayland"

FILES_${PN} += "${libdir}/gstreamer-0.10/*.so"
FILES_${PN}-dbg += "${libdir}/gstreamer-0.10/.debug"
FILES_${PN}-dev += "${libdir}/gstreamer-0.10/*.la ${libdir}/gstreamer-0.10/*.a"
