DESCRIPTION = "An Assortment of Node Test Applications"
HOMEPAGE = "http://127.0.0.1/dev/urandom"
LICENSE = "BSD"

LIC_FILES_CHKSUM = "file://LICENSE;md5=d8415ca00f8ed4a40f1f16ebcc4b570e"

DEPENDS = "nodejs-native"
RDEPENDS_${PN} = "nodejs"

SRC_URI = "file://event-catch.js \
           file://event-send.js \
           file://list-apps.js \
           file://package.json \
           file://LICENSE \
           file://iot-node-test.manifest \
"

IOT_APP_PROVIDER = "finedine"

# use iot-app support class
inherit iot-app

S = "${WORKDIR}/"

# we don't care about debug for the few binary node modules
INHIBIT_PACKAGE_DEBUG_SPLIT = "1"
INSANE_SKIP_${PN} = "staticdev"

# manual install before npm-install.bbclass lands

do_install () {
    mkdir -p ${D}${IOT_APP_INSTALLATION_PATH}
    cp event-catch.js event-send.js list-apps.js package.json LICENSE ${D}${IOT_APP_INSTALLATION_PATH}
    mkdir -p ${D}${IOT_APP_MANIFEST_PATH}/
    cp iot-node-test.manifest ${D}${IOT_APP_MANIFEST_PATH}/${PN}.manifest
    #install -D -m 755 ${S}/example-app-launch ${D}${IOT_APP_TLM_PATH}/tlm-launch
    #chown ${IOT_APP_PROVIDER}.${IOT_APP_PROVIDER} ${D}${IOT_APP_TLM_PATH}/tlm-launch
}

FILES_${PN} = "${IOT_APP_INSTALLATION_PATH}"
FILES_${PN} += "${IOT_APP_MANIFEST_PATH}/${PN}.manifest"

PACKAGES = "${PN}"
