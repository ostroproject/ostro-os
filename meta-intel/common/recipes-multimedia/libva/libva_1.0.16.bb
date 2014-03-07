require libva.inc

PACKAGECONFIG[x11] = ",,virtual/libx11 libxext libxfixes"
PACKAGECONFIG[wayland] = ",,"

PR = "${INC_PR}.0"

SRC_URI = "http://www.freedesktop.org/software/vaapi/releases/libva/libva-${PV}.tar.bz2"

SRC_URI[md5sum] = "99343b27cf24e99abc0c5db2d09e30c8"
SRC_URI[sha256sum] = "03e46f8f48f252e6b6112c495745100bc217ddded801fdb393384aab1fafeaa2"
