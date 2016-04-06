DESCRIPTION = "AppFW Test App"
HOMEPAGE = "http://example.com"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://COPYING.MIT;md5=838c366f69b72c5df05c96dff79b35f2"

OSTRO_USER_NAME = "appfwtest"
OSTRO_APP_NAME = "commonapp"

SRC_URI = "file://wrapperapp \
           file://COPYING.MIT \
           file://manifest \
"

inherit ostro-app

S = "${WORKDIR}/"

do_install () {
    install -d ${D}${OSTRO_APP_ROOT}/bin
    install -d ${D}${OSTRO_APP_ROOT}/usr/share
    install -m 0755 wrapperapp  ${D}${OSTRO_APP_ROOT}/bin/
    install -m 0644 COPYING.MIT ${D}${OSTRO_APP_ROOT}/usr/share/
    install -m 0644 manifest ${D}${OSTRO_APP_ROOT}/
}

FILES_${PN} = "${OSTRO_APP_ROOT}/bin/wrapperapp"
FILES_${PN} =+ "${OSTRO_APP_ROOT}/manifest"
FILES_${PN} =+ "${OSTRO_APP_ROOT}/usr/share/COPYING.MIT"
