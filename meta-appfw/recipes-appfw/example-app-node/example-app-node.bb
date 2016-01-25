DESCRIPTION = "Example Node application"
HOMEPAGE = "http://example.com"
LICENSE = "MIT"

LIC_FILES_CHKSUM = "file://COPYING.MIT;md5=838c366f69b72c5df05c96dff79b35f2"

DEPENDS = "nodejs-native"
RDEPENDS_${PN} += "nodejs"

SRC_URI = "file://example.js \
           file://package.json \
           file://COPYING.MIT \
           file://manifest \
"

OSTRO_USER_NAME = "iodine"
OSTRO_APP_NAME = "nodetest"

# use ostro-app support class
inherit ostro-app

S = "${WORKDIR}/"

# we don't care about debug for the few binary node modules
INHIBIT_PACKAGE_DEBUG_SPLIT = "1"
INSANE_SKIP_${PN} = "staticdev"

# manual install before npm-install.bbclass lands

do_install () {
    mkdir -p ${D}${OSTRO_APP_ROOT}/lib/node_modules/${OSTRO_APP_NAME}
    cp example.js package.json COPYING.MIT ${D}${OSTRO_APP_ROOT}/lib/node_modules/${OSTRO_APP_NAME}/
    cp manifest ${D}${OSTRO_APP_ROOT}/manifest
}

FILES_${PN} = "${OSTRO_APP_ROOT}/lib/node_modules/${OSTRO_APP_NAME}"
FILES_${PN} += "${OSTRO_APP_ROOT}/manifest"

PACKAGES = "${PN}"
