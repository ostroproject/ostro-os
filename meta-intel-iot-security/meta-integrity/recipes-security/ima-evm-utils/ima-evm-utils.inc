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
RDEPENDS_${PN} += "util-linux-blkid"

# Documentation depends on asciidoc, which we do not have, so
# do not build documentation.

inherit autotools
