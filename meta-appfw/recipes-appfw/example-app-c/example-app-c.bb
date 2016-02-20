DESCRIPTION = "Example native application"
HOMEPAGE = "http://example.com"
LICENSE = "MIT"

LIC_FILES_CHKSUM = "file://COPYING.MIT;md5=838c366f69b72c5df05c96dff79b35f2"

OSTRO_USER_NAME = "yoyodine"
OSTRO_APP_NAME = "nativetest"

PACKAGECONFIG ??= "default"
PACKAGECONFIG[default] = "--with-manifest-path=${OSTRO_APP_ROOT}"

SRC_URI = "file://aclocal.m4                    \
           file://bootstrap                     \
           file://configure.ac                  \
           file://Makefile.am                   \
           file://build-aux/shave.in            \
           file://build-aux/shave-libtool.in    \
           file://m4/libtool.m4                 \
           file://m4/lt~obsolete.m4             \
           file://m4/ltoptions.m4               \              
           file://m4/ltsugar.m4                 \
           file://m4/ltversion.m4               \
           file://m4/shave.m4                   \
           file://src/hello-world.c             \
           file://src/manifest.in               \
           file://src/Makefile.am               \
           file://COPYING.MIT"

inherit autotools pkgconfig ostro-app

S = "${WORKDIR}"

INHIBIT_PACKAGE_DEBUG_SPLIT = "1"

PACKAGES = "${PN}"
