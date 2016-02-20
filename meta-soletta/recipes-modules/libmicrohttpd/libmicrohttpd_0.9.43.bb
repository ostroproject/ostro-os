DESCRIPTION = "A small C library that is supposed to make it easy to run an HTTP server as part of another application"
HOMEPAGE = "http://www.gnu.org/software/libmicrohttpd/"
LICENSE = "LGPL-2.1+"
LIC_FILES_CHKSUM = "file://COPYING;md5=9331186f4f80db7da0e724bdd6554ee5"
SECTION = "net"
DEPENDS = "libgcrypt gnutls file"

SRC_URI[md5sum] = "23d5ee02cc9f16bff676b3c460b7b602"
SRC_URI[sha256sum] = "414bb37471fd91646a7a41c6877a5be2d03871e8d9f845fd3ee55d0970d9069f"

SRC_URI = "http://ftp.gnu.org/gnu/libmicrohttpd/${BPN}-${PV}.tar.gz"

inherit autotools lib_package pkgconfig

# disable spdy, because it depends on openssl
EXTRA_OECONF += "--disable-static --with-gnutls=${STAGING_LIBDIR}/../ --disable-spdy"

PACKAGECONFIG ?= "curl"
PACKAGECONFIG_append_class-target = "\
        ${@base_contains('DISTRO_FEATURES', 'largefile', 'largefile', '', d)} \
"
PACKAGECONFIG[largefile] = "--enable-largefile,--disable-largefile,,"
PACKAGECONFIG[curl] = "--enable-curl,--disable-curl,curl,"

do_compile_append() {
	sed -i s:-L${STAGING_LIBDIR}::g libmicrohttpd.pc
}

