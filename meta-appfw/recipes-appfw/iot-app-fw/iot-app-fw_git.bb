DESCRIPTION = "Application framework daemon and client"
HOMEPAGE = "http://github.com/01org/iot-app-fw"
LICENSE = "BSD-3-Clause"

LIC_FILES_CHKSUM = "file://LICENSE-BSD;md5=f9f435c1bd3a753365e799edf375fc42"

DEPENDS = "json-c"

SRC_URI = " \
    git://git@github.com/ostroproject/iot-app-fw.git;protocol=ssh \
  "

SRCREV = "0e954664774ad33ec5718fd94ef35c8b551cb8be"

inherit autotools pkgconfig systemd

AUTO_LIBNAME_PKGS = ""

S = "${WORKDIR}/git"

# possible package configurations
PACKAGECONFIG ??= ""
PACKAGECONFIG[qt]         = "--enable-qt,--disable-qt,qt4-x11-free"
PACKAGECONFIG[pulse]      = "--enable-pulse,--disable-pulse,pulseaudio"
PACKAGECONFIG[glib-2.0]   = "--enable-glib,--disable-glib,glib-2.0"
PACKAGECONFIG[shave]      = "--enable-shave,--disable-shave"

PACKAGES =+ "${PN}-launcher"
FILES_${PN}-launcher = "${bindir}/iot-launch-daemon"
FILES_${PN}-launcher += "${bindir}/iot-launch"
FILES_${PN}-launcher += "${libdir}/iot-app-fw"
FILES_${PN}-launcher += "${systemd_unitdir}/system"

PACKAGES =+ "${PN}-test"
FILES_${PN}-test = "${bindir}/iot-event-test"
