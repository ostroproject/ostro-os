DESCRIPTION = "a Python interface for the Firmata protocol"
SECTION = "devel/python"
LICENSE = "BSD"
LIC_FILES_CHKSUM = "file://LICENSE;md5=84ddcef430b7c44caa22b2ff4b37a3df"
SRCNAME = "pyFirmata"

SRC_URI = "https://pypi.python.org/packages/source/p/${SRCNAME}/${SRCNAME}-${PV}.tar.gz"
S = "${WORKDIR}/${SRCNAME}-${PV}"

RDEPENDS_${PN} = "\
    python-pyserial \
"

SRC_URI[md5sum] = "6f9e9a617ffb904c6eb4f5b4696790db"
SRC_URI[sha256sum] = "01531fea95aa2585aa49a48474d0e0046add38baefa6b7944393f503eb05322f"

inherit distutils
