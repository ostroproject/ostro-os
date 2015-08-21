SUMMARY = "memory measurement tool"
DESCRIPTION = "a tool to give a reasonable per application memory footprint estimate"
LICENSE = "GPLv2"
DEPENDS = "glib-2.0"
LIC_FILES_CHKSUM = "file://memuse.c;beginline=10;endline=13;md5=ad50b71ddf9f398698079718b406523c"

SRC_URI = "git://github.com/vslm698/memuse.git;protocal=http"
SRCREV = "e3d092c2ccaca413783666e8e7889435be71e748"
S = "${WORKDIR}/git"

CFLAGS_append = " `pkg-config --cflags --libs glib-2.0` "
EXTRA_OEMAKE = " 'CC=${CC}' 'CFLAGS=${CFLAGS}' "

do_install() {
    # The existing Makefile hard-codes /usr/bin. Instead of patching it,
    # just install the binary ourselves.
    install -D memuse ${D}/${bindir}/memuse
}
