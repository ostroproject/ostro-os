DESCRIPTION = "Logging service"
LICENSE = "Apache-2.0"
LIC_FILES_CHKSUM = "file://LICENSE.APLv2;md5=b8c413dab2ff689b6e48821205d4d364"

DEPENDS = " \
systemd \
pkgconfig \
tizen-platform-config \
"

inherit autotools
