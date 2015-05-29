DESCRIPTION = "IMA/EVM control utility"
LICENSE = "GPL-2.0-with-OpenSSL-exception"
LIC_FILES_CHKSUM = "file://COPYING;md5=b234ee4d69f5fce4486a80fdaf4a4263"

DEPENDS = " \
openssl \
attr \
keyutils \
pkgconfig \
"

# blkid is called by evmctl when creating evm checksums.
# This is less useful when signing files on the build host,
# so disable it when compiling on the host.
RDEPENDS_${PN}_append_class-target = " util-linux-blkid"

inherit autotools

BBCLASSEXTEND = "native"
