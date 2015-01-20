require gstreamer-vaapi.inc

DEPENDS += "gstreamer gst-plugins-base gst-plugins-bad"

GST_API_VERSION = "0.10"

PACKAGECONFIG_remove = "wayland"
