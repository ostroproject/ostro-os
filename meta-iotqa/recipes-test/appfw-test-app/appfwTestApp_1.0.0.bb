DESCRIPTION = "AppFW Test app"
LICENSE = "MIT"

LIC_FILES_CHKSUM = "file://COPYING.MIT;md5=838c366f69b72c5df05c96dff79b35f2"


SRC_URI = "file://appfwTestApp.sh \
           file://appfwTestApp.manifest \
           file://COPYING.MIT"

IOT_APP_PROVIDER = "appfwtest"

# use iot-app support class
inherit iot-app

S = "${WORKDIR}/"

INHIBIT_PACKAGE_DEBUG_SPLIT = "1"
INSANE_SKIP_${PN} = "staticdev"

do_install () {
    mkdir -p ${D}${IOT_APP_INSTALLATION_PATH}
    mkdir -p ${D}${IOT_APP_MANIFEST_PATH}
    chmod +x appfwTestApp.sh
    cp appfwTestApp.sh ${D}${IOT_APP_INSTALLATION_PATH}/
    cp appfwTestApp.manifest ${D}${IOT_APP_MANIFEST_PATH}/${PN}.manifest
}

FILES_${PN} = "${IOT_APP_INSTALLATION_PATH}/appfwTestApp.sh"
FILES_${PN} += "${IOT_APP_MANIFEST_PATH}/${PN}.manifest"

PACKAGES = "${PN}"
