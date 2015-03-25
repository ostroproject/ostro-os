SUMMARY = "Transparently implements the necessary message formats and transport security as well as device registration"
SECTION = "libs"
HOMEPAGE = "http://enableiot.com"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://COPYING;md5=e8db6501ed294e65418a933925d12058"

DEPENDS = "nodejs-native swig-native curl"

SRC_URI = "git://github.com/enableiot/iotkit-lib-c.git;protocol=https"
SRCREV = "eaa4af960ffda40c0ca6eca80c18c61f415ef685"

S = "${WORKDIR}/git"

EXTRA_OECMAKE += " -DSTAGING_DIR_TARGET=${STAGING_DIR_TARGET}"

inherit distutils-base pkgconfig python-dir cmake

do_compile_prepend () {
    # when yocto builds in ${D} it does not have access to ../git/.git so git
    # describe --tags fails. In order not to tag our version as dirty we use this
    # trick
    sed -i 's/-dirty//' src/version.c
}

do_install_prepend () {
    # Copy config file
    install -d ${D}${sysconfdir}/iotkit-lib
    install -d ${D}${datadir}/iotkit-lib
    install -m 644 ${S}/config/config.json ${D}${sysconfdir}/iotkit-lib/

    # Copy test programs
    cp -r ${B}/tests/ ${D}${datadir}/iotkit-lib/
    rm -rf ${D}${datadir}/iotkit-lib/tests/CMakeFiles/
    touch ${D}${datadir}/iotkit-lib/.setup.done
}

PACKAGES =+ "${PN}-tests"

FILES_${PN}-dbg += "${libdir}/node_modules/iotkitjs/.debug/ \
                    ${libdir}/python2.7/dist-packages/.debug/ \
                    ${datadir}/iotkit-lib/tests/.debug/"

FILES_${PN}-tests = "${datadir}/iotkit-lib/tests/*"

FILES_${PN} += "${sysconfdir} \
                ${datadir}/iotkit-lib/.setup.done"

RDEPENDS_${PN}-tests += "${PN} gcov cmake"
