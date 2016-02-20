DESCRIPTION = "Example Python application"
HOMEPAGE = "http://example.com"
LICENSE = "MIT"

LIC_FILES_CHKSUM = "file://COPYING.MIT;md5=838c366f69b72c5df05c96dff79b35f2"

RDEPENDS_${PN} += "python"

SRC_URI = "file://example.py \
           file://COPYING.MIT \
           file://manifest \
"

OSTRO_USER_NAME = "foodine"
OSTRO_APP_NAME = "pythontest"

# use ostro-app support class
inherit ostro-app

S = "${WORKDIR}/"

do_install () {
    mkdir -p ${D}${OSTRO_APP_ROOT}/lib/python/${OSTRO_APP_NAME}
    cp example.py COPYING.MIT ${D}${OSTRO_APP_ROOT}/lib/python/${OSTRO_APP_NAME}/
    cp manifest ${D}${OSTRO_APP_ROOT}/manifest
}


FILES_${PN} = "${OSTRO_APP_ROOT}/lib/python/${OSTRO_APP_NAME}/example.py"
FILES_${PN} += "${OSTRO_APP_ROOT}/lib/python/${OSTRO_APP_NAME}/COPYING.MIT"
FILES_${PN} += "${OSTRO_APP_ROOT}/manifest"
