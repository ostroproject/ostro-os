DESCRIPTION = "U-boot bootloader mkimage tool"
LICENSE = "GPLv2+"
LIC_FILES_CHKSUM = "file://Licenses/README;md5=025bf9f768cbcb1a165dbe1a110babfb"
SECTION = "bootloader"

require u-boot-internal.inc

EXTRA_OEMAKE = 'HOSTCC="${CC}" HOSTLD="${LD}" HOSTLDFLAGS="${LDFLAGS}" HOSTSTRIP=true'

do_compile () {
  oe_runmake tools
}

do_install () {
  install -d ${D}${bindir}
  install -m 0755 tools/mkimage ${D}${bindir}/uboot-mkimage
  install -m 0755 tools/mkenvimage ${D}${bindir}/uboot-mkenvimage
  ln -sf uboot-mkimage ${D}${bindir}/mkimage
  ln -sf uboot-mkenvimage ${D}${bindir}/mkenvimage
}

BBCLASSEXTEND = "native nativesdk"
