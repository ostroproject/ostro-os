DESCRIPTION = "Tizen Platform Configuration"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://MIT;md5=89df1e71994f36ecaefe566c071db3e8;beginline=5"

inherit autotools

DEPENDS = " \
tizen-platform-wrapper \
tizen-platform-wrapper-native \
"

EXTRA_OECONF += " --enable-static"
