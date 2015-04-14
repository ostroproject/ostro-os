DESCRIPTION = "helper library for wyliodrin nodejs server"
HOMEPAGE = "http://github.com/Wyliodrin/libwyliodrin"
LICENSE = "BSD-3-Clause"
SECTION = "libs"
DEPENDS = "redis"
PR = "r0"

LIC_FILES_CHKSUM = "file://COPYING;md5=d84d659a35c666d23233e54503aaea51"
SRC_URI = "git://github.com/redis/hiredis;protocol=git;rev=0fff0f182b96b4ffeee8379f29ed5129c3f72cf7 \
           file://0001-Makefile-remove-hardcoding-of-CC.patch"

S = "${WORKDIR}/git"

inherit autotools

do_compile() {
  cd ${S}
  oe_runmake
}

do_install() {
  cd ${S}
  oe_runmake PREFIX=${D}/usr install
}
