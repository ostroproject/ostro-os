require gstreamer-vaapi.inc

DEPENDS += "gstreamer1.0 gstreamer1.0-plugins-base gstreamer1.0-plugins-bad"

GST_API_VERSION = "1.4"

SRC_URI += "file://0001-libs-remove-unneeded-headers.patch"

SRC_URI[md5sum] = "f01425481bd161f57334dab7ab4069d3"
SRC_URI[sha256sum] = "36fc8afeb7ec679ea8df34671a34dba57dcc0b66255fb0991acb485e3efd67b3"
