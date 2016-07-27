SUMMARY = "swupd sofware update from Clear Linux - server component"
HOMEPAGE = "https://github.com/clearlinux/swupd-server"
LICENSE = "GPL-2.0"
LIC_FILES_CHKSUM = "file://COPYING;md5=f8d90fb802930e30e49c39c8126a959e"

DEPENDS = "file glib-2.0 rsync openssl libarchive bsdiff bzip2"
DEPENDS_append_class-native = " bzip2-replacement-native"

PV = "3.2.5+git${SRCPV}"
SRC_URI = "\
    git://github.com/clearlinux/swupd-server.git;protocol=https \
    file://fullfiles.c-work-around-pseudo-bug.patch \
"
SRCREV = "ddca171dad32229ceeff8b8527a179610b88ce55"

S = "${WORKDIR}/git"

inherit pkgconfig autotools

EXTRA_OECONF = "--enable-bzip2 --enable-lzma --disable-stateless --disable-tests --enable-bsdtar"

# safer-calls-to-system-utilities.patch uses for loop initial declaration
CFLAGS_append = " -std=c99"

RDEPENDS_${PN} = "rsync"
RDEPENDS_${PN}_class-target = " bsdtar"

BBCLASSEXTEND = "native"
