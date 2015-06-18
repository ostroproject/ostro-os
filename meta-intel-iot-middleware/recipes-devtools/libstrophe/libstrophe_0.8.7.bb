DESCRIPTION = "Libstrophe"
HOMEPAGE = "http://github.com/strophe/wyliodrin-server"
LICENSE = "GPLv3"

LIC_FILES_CHKSUM = "file://LICENSE.txt;md5=892237188a4b8b82aa29dddb2ae496fb"

DEPENDS = "libxml2 expat openssl"

SRC_URI = "git://github.com/strophe/libstrophe;protocol=git;rev=2093aac817cfd37fcbcd8465af6234280a383961"

S = "${WORKDIR}/git"

inherit autotools pkgconfig
