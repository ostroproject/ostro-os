require libva-intel-driver.inc

PR = "${INC_PR}.0"

SRC_URI = "http://www.freedesktop.org/software/vaapi/releases/libva-intel-driver/libva-intel-driver-${PV}.tar.bz2"

SRC_URI += "file://0001-Workaround-for-concurrently-playing-VC1-and-H264-vid.patch"

SRC_URI[md5sum] = "13907085223d88d956cdfc282962b7a7"
SRC_URI[sha256sum] = "789fa2d6e22b9028ce12a89981eb33e57b04301431415149acfb61a49d3a63ee"
