SUMMARY = "Binary delta tools and library"
HOMEPAGE = "https://github.com/clearlinux/bsdiff"
LICENSE = "BSD"
LIC_FILES_CHKSUM = "file://COPYING;md5=0dbe7a50f028269750631fcbded3846a"

SRC_URI = "git://github.com/clearlinux/bsdiff.git;protocol=https"

PV = "1.0.1+git${SRCPV}"
SRCREV = "8c0a87b7c9eb5b22ed4e03a4eb42b32bd390df14"

S = "${WORKDIR}/git"

DEPENDS = "xz bzip2 zlib libcheck"

inherit pkgconfig autotools

EXTRA_OECONF = "--disable-tests"

BBCLASSEXTEND = "native"
