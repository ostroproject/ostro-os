require libva-intel-driver.inc

SRC_URI = "http://www.freedesktop.org/software/vaapi/releases/libva-intel-driver/libva-intel-driver-${PV}.tar.bz2"

SRC_URI += "file://0001-Workaround-for-concurrently-playing-VC1-and-H264-vid.patch"

SRC_URI[md5sum] = "afdd4c91ac552a14b4d0ce93b75c88bb"
SRC_URI[sha256sum] = "a6fceaa118fe5d1a6e7382ed30e6684b4059b3fedd79eb53121a80e8016c748c"
