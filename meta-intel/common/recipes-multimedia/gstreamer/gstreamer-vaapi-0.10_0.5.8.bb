require gstreamer-vaapi.inc

DEPENDS += "gstreamer gst-plugins-base gst-plugins-bad"

GST_API_VERSION = "0.10"

SRC_URI += "file://gstvideoencoder.c file://gstvideoencoder.h"

PACKAGECONFIG_remove = "wayland"

# SRC_URI subdir parameter is broken for files, when fixed do the move there
do_compile_prepend() {
	cp -f ${WORKDIR}/gstvideoencoder.[ch] ${S}/ext/videoutils/gst-libs/gst/video/
}
