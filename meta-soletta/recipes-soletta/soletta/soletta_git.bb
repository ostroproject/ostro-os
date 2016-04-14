#
# soletta.bb
#

DESCRIPTION = "Soletta library and modules"
SECTION = "examples"
DEPENDS = "glib-2.0 libpcre pkgconfig python3-jsonschema-native icu curl libmicrohttpd mosquitto"
DEPENDS += " ${@bb.utils.contains('DISTRO_FEATURES','systemd','systemd','',d)}"
LICENSE = "Apache-2.0"
LIC_FILES_CHKSUM = "file://LICENSE;md5=93888867ace35ffec2c845ea90b2e16b"
PV = "1_beta18+git${SRCPV}"

SRC_URI = "gitsm://github.com/solettaproject/soletta.git;protocol=git \
           file://run-ptest \
           file://0013-lib-sol-iio-release-buffer-on-sol_iio_close.patch \
           file://0047-oic-gen-fix-rep_vec-issue.patch \
           file://0048-oic-gen-ReadOnly-props-from-imported-json-objs-were-.patch \
           file://0049-oic-gen-Don-t-add-client-to_repr_vec-when-all-props-.patch \
           file://0050-oic-gen-Always-generate-code-using-same-order-of-res.patch \
           file://i2c-dev.conf \
           file://iio-trig-sysfs.conf \
          "
SRCREV = "97091af414193c37278ba5ff88c70c596eecd7ea"

S = "${WORKDIR}/git"

inherit cml1 python3native

PACKAGES = " \
         ${PN}-staticdev \
         ${PN}-dev \
         ${PN}-dbg \
         ${PN} \
"

FILES_${PN}-staticdev = " \
                      ${libdir}/libsoletta.a \
"

FILES_${PN}-dbg = " \
                 ${datadir}/gdb \
"

FILES_${PN}-dev = " \
                ${datadir}/soletta/* \
                ${includedir}/soletta/* \
                ${libdir}/pkgconfig/soletta.pc \
                ${libdir}/soletta/modules/flow/* \
                ${libdir}/soletta/modules/pin-mux/* \
                ${libdir}/soletta/modules/linux-micro/* \
                ${libdir}/soletta/modules/flow-metatype/* \
                ${sysconfdir}/modules-load.d/* \
"

FILES_${PN} = " \
            ${bindir}/sol* \
            ${libdir}/libsoletta.so* \
            ${libdir}/soletta/soletta-image-hash \
"

# Setup what PACKAGES should be installed by default.
# If a package should not being installed, use BAD_RECOMMENDS.
RRECOMMENDS_${PN} = "\
                  ${PN} \
                  ${PN}-dev \
"

# since we only enable flow-module-udev only with systemd feature
# can can disable the RDEPENDS based on the same criteria
RDEPENDS_${PN} = " \
             ${@bb.utils.contains('DISTRO_FEATURES','systemd','libudev','',d)} \
             chrpath \
             libpcre \
"

# do_package_qa tells soletta rdepends on soletta-dev
# maybe an non-obvious implicit rule implied by yocto
INSANE_SKIP_${PN} += "dev-deps file-rdeps"
INHIBIT_PACKAGE_STRIP = "1"
INHIBIT_DEFAULT_DEPS = "1"

B = "${WORKDIR}/git"

do_configure_prepend() {
   export TARGETCC="${CC}"
   export TARGETAR="${AR}"
}

do_compile() {
   oe_runmake CFLAGS="--sysroot=${STAGING_DIR_TARGET} -pthread -lpcre" TARGETCC="${CC}" TARGETAR="${AR}"
}

do_install() {
   oe_runmake DESTDIR=${WORKDIR}/image install CFLAGS="--sysroot=${STAGING_DIR_TARGET}" TARGETCC="${CC}" TARGETAR="${AR}"
   unlink ${WORKDIR}/image/usr/lib/libsoletta.so
   mv ${WORKDIR}/image/usr/lib/libsoletta.so.0.0.1 ${WORKDIR}/image/usr/lib/libsoletta.so
   ln -sf libsoletta.so ${WORKDIR}/image/usr/lib/libsoletta.so.0.0.1
   COMMIT_ID=`git --git-dir=${WORKDIR}/git/.git rev-parse --verify HEAD`
   echo "Soletta: $COMMIT_ID" > ${D}/usr/lib/soletta/soletta-image-hash
}

do_install_append() {
   install -d ${D}${sysconfdir}/modules-load.d
   install -m 0644 ${WORKDIR}/i2c-dev.conf ${D}${sysconfdir}/modules-load.d
   install -m 0644 ${WORKDIR}/iio-trig-sysfs.conf ${D}${sysconfdir}/modules-load.d
}

inherit ptest

do_compile_ptest() {
        oe_runmake TARGETCC="${CC}" TARGETAR="${AR}" "tests"
}

do_install_ptest () {
        mkdir -p ${D}/${PTEST_PATH}/src
        cp -rf ${S}/build/stage/test ${D}/${PTEST_PATH}/src/
        cp -f ${S}/data/scripts/suite.py ${D}/${PTEST_PATH}
        cp -rf ${S}/src/test-fbp ${D}/${PTEST_PATH}/src/
        cp -f ${S}/tools/run-fbp-tests ${D}/${PTEST_PATH}

}
