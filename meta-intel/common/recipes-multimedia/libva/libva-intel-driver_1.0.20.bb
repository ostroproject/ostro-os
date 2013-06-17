require libva-intel-driver.inc

SRC_URI = "http://www.freedesktop.org/software/vaapi/releases/libva-intel-driver/libva-intel-driver-${PV}.tar.bz2"

SRC_URI += "file://0001-Workaround-for-concurrently-playing-VC1-and-H264-vid.patch"

SRC_URI[md5sum] = "55b8e5d1126cc0f7e9df968017d21468"
SRC_URI[sha256sum] = "12fefb661372c053ff26530fae8342f9df63dbe8ab2c548d8d430d994042d4c9"
