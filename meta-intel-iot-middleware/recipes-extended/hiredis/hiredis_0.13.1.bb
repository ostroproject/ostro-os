DESCRIPTION = "inimalistic C client library for Redis"
HOMEPAGE = "http://github.com/redis/hiredis"
LICENSE = "BSD-3-Clause"
SECTION = "libs"
DEPENDS = "redis"
PR = "r0"

LIC_FILES_CHKSUM = "file://COPYING;md5=d84d659a35c666d23233e54503aaea51"
SRC_URI = "git://github.com/redis/hiredis;protocol=git;rev=f58dd249d6ed47a7e835463c3b04722972281dbb \
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
  cp hiredis.pc ${D}/${libdir}/pkgconfig/
}
