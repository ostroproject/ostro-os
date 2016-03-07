SUMMARY = "swupd sofware update from Clear Linux - server component"
HOMEPAGE = "https://github.com/clearlinux/swupd-server"
LICENSE = "GPL-2.0"
LIC_FILES_CHKSUM = "file://COPYING;md5=f8d90fb802930e30e49c39c8126a959e"

DEPENDS = "file xz glib-2.0 zlib bzip2 tar rsync openssl bsdiff"

PV = "3.1.2+git${SRCPV}"
SRC_URI = "\
    git://github.com/clearlinux/swupd-server.git;protocol=https \
"
SRCREV = "51c0bf200792b19593782bf819bbc3d239ec0b50"

S = "${WORKDIR}/git"

inherit autotools

EXTRA_OECONF = "--enable-bzip2 --enable-lzma --disable-stateless --disable-tests"

# safer-calls-to-system-utilities.patch uses for loop initial declaration
CFLAGS_append = " -std=c99"

RDEPENDS_${PN} = "tar rsync"

BBCLASSEXTEND = "native"
