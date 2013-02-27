require libva-intel-driver.inc

PR = "${INC_PR}.0"

SRC_URI = "http://www.freedesktop.org/software/vaapi/releases/libva-intel-driver/libva-intel-driver-${PV}.tar.bz2"

SRC_URI += "file://0001-Workaround-for-concurrently-playing-VC1-and-H264-vid.patch"

SRC_URI[md5sum] = "a4a668c86ef8c9fb3bde087857d74bf6"
SRC_URI[sha256sum] = "2db68da9f4cea9b726ce2cd7c6246d902085310d83609082e453aa01559ea792"
