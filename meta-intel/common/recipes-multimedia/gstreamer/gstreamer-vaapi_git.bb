SUMMARY = "VA-API support to GStreamer"
DESCRIPTION = "gstreamer-vaapi consists of a collection of VA-API \
based plugins for GStreamer and helper libraries: `vaapidecode', \
`vaapiconvert', and `vaapisink'."

LICENSE = "LGPLv2.1+"
LIC_FILES_CHKSUM = "file://COPYING.LIB;md5=4fbd65380cdd255951079008b364516c"

DEPENDS = "gstreamer gst-plugins-base gst-plugins-bad libva"

# 0.4.0 tag
SRCREV = "329065546463512c8cc9c92c7f34510793ceb6dd"
PV = "0.4.0+git${SRCPV}"
PR = "r0"

SRC_URI = "git://gitorious.org/vaapi/gstreamer-vaapi.git"

SRC_URI[md5sum] = "729d75f21df79114a8c81d896489e5ad"
SRC_URI[sha256sum] = "f1770c4537f1615701dbc845eee5732fbb1036b3acafbc7488e551fab334a31d"

S = "${WORKDIR}/git"

inherit autotools pkgconfig gtk-doc

EXTRA_OECONF = "--disable-ffmpeg"

do_configure_prepend() {
  # DEBUG: Executing shell function do_configure
  # ln: target `m4/' is not a directory: No such file or directory
  # cp: cannot create regular file `m4/': Not a directory
  # (should be fixed in autotools.bbclass)
  mkdir --parents ${B}/m4
}

FILES_${PN} += "${libdir}/gstreamer-0.10/*.so"
FILES_${PN}-dbg += "${libdir}/gstreamer-0.10/.debug"
FILES_${PN}-dev += "${libdir}/gstreamer-0.10/*.la ${libdir}/gstreamer-0.10/*.a"
