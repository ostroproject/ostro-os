require gstreamer-vaapi.inc

DEPENDS += "gstreamer1.0 gstreamer1.0-plugins-base gstreamer1.0-plugins-bad"

SRC_URI[md5sum] = "ce2d4921b8d9c78edd609d95e8c502d3"
SRC_URI[sha256sum] = "abe8ea4dfb3177d038b38610537c651b943707ed110882782a19b95a9ea04a92"

SRC_URI =+ "file://0001-decoder-h265-Fix-offset-calculation-in-codec_data-pa.patch"
