require gstreamer-vaapi.inc

DEPENDS += "gstreamer gst-plugins-base gst-plugins-bad"

SRC_URI += "file://wayland-compile.patch"

GST_API_VERSION = "0.10"
