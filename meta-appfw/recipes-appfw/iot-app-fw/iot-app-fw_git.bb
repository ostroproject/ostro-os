DESCRIPTION = "Revised mininal application 'framework'."
HOMEPAGE = "http://github.com/01org/iot-app-fw"
LICENSE = "BSD-3-Clause"

LIC_FILES_CHKSUM = "file://LICENSE-BSD;md5=f9f435c1bd3a753365e799edf375fc42"

DEPENDS = "json-c systemd"

SRC_URI = " \
    git://git@github.com/ostroproject/iot-app-fw.git;protocol=ssh;branch=kli/devel/systemd-generator \
  "

SRCREV = "b558c68a21f2649713cbeca3cf1fb6ac3199f9f8"

inherit autotools pkgconfig systemd

AUTO_LIBNAME_PKGS = ""

S = "${WORKDIR}/git"

# possible package configurations
PACKAGECONFIG ??= ""
PACKAGECONFIG[glib-2.0] = "--enable-glib,--disable-glib,glib-2.0"
PACKAGECONFIG[shave]    = "--enable-shave,--disable-shave"

FILES_${PN}     =  "/lib/systemd/system-generators/iot-service-generator"
FILES_${PN}-dbg =+ "/lib/systemd/system-generators/.debug"
