DESCRIPTION = "NAUI: (Not a UI) A tool to generate a webpage with useful platform information"
SECTION = "utils"

LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://COPYING;md5=ae9b2c90ad4abb07ea936beca1c75fce"

DEPENDS = "libxml2"

SRC_URI = "file://${BP}.tar.bz2 \
           file://naui"

SRC_URI[md5sum] = "d866413d1252cfa2022063504c9f9b57"
SRC_URI[sha256] = "e573221aa047ae27e9fad08e1db5152fe942d98e67b2fd77c0cd380e7ccb023c"

inherit distutils-base pkgconfig cmake

do_install() {
          install -d ${D}${bindir}
          install -d ${D}${datadir}/naui/
	  
          install -m 0755 naui ${D}${bindir}/
          install -m 0644 index.html ${D}${datadir}/naui/

          install -d ${D}${sysconfdir}/init.d/
          install -m 0755 ${WORKDIR}/naui ${D}${sysconfdir}/init.d/
}

inherit update-rc.d

INITSCRIPT_NAME = "naui"
INITSCRIPT_PARAMS = "defaults 99"

FILES_${PN} = "${bindir}/ \
               ${datadir}/ \
               ${sysconfdir}/init.d/"
