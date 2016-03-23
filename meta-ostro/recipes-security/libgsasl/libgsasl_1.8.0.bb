SUMMARY = "GNU SASL Library"
DESCRIPTION = "GNU SASL is an implementation of the Simple Authentication and Security Layer framework and a few common SASL mechanisms. SASL is used by network servers (e.g., IMAP, SMTP) to request authentication from clients, and in clients to authenticate against servers."

DEPENDS = "virtual/gettext libidn"
RDEPENDS_${PN} = "libidn"

LICENSE = "GPLv2+ & LGPLv2.1+"
LIC_FILES_CHKSUM = " \
	file://COPYING;md5=d32239bcb673463ab874e80d47fae504 \
	file://COPYING.LIB;md5=4fbd65380cdd255951079008b364516c \
	"

SRC_URI = " \
	ftp://ftp.gnu.org/gnu/gsasl/libgsasl-1.8.0.tar.gz \
	file://0001-configure.ac-add-missing-AM_PROG_AR.patch \
	"
SRC_URI[md5sum] = "5dbdf859f6e60e05813370e2b193b92b"

inherit pkgconfig autotools

