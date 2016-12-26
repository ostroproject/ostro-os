SUMMARY = "Applications and Scripts for libyami."
DESCRIPTION = "Applications and Scripts for libyami."

HOMEPAGE = "https://github.com/01org/libyami-utils"
BUGTRACKER = "https://github.com/01org/libyami-utils/issues/new"

LICENSE = "Apache-2.0"
LIC_FILES_CHKSUM = "file://LICENSE;md5=e3fc50a88d0a364313df4b21ef20c29e"

SRC_URI = "https://github.com/01org/libyami-utils/archive/${PV}.tar.gz"

SRC_URI[md5sum] = "51420c8ddcecac1e24a238c43e2e18ca"
SRC_URI[sha256sum] = "a5826a5ade885dc33e1a7d23f5f261522f88661ee486d3b8bbff6bdfaacf2495"

S = "${WORKDIR}/libyami-utils-${PV}"

DEPENDS = "libva libyami"

EXTRA_OECONF = " --enable-tests-gles --disable-md5"

inherit autotools pkgconfig
