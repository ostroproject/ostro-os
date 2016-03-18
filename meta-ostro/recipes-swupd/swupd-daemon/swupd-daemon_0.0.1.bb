SUMMARY = "D-Bus service daemon for Clear Linux swupd-client"
DESCRIPTION = "Daemon providing system-bus D-Bus API for utilizing Clear Linux swupd-client functionality."

DEPENDS = "glib-2.0"
RDEPENDS_${PN} = "glib-2.0"

LICENSE = "LGPLv2.1+"
LIC_FILES_CHKSUM = "file://COPYING;md5=4fbd65380cdd255951079008b364516c"

SRC_URI = "git://github.com/ostroproject/swupd-daemon.git;protocol=https"
SRCREV = "0cca14cc3298ee804c414da7ed65863e91c171bc"

S = "${WORKDIR}/git"

inherit pkgconfig autotools

