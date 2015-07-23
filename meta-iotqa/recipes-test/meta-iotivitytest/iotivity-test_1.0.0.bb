inherit scons

SUMMARY = "Iotivity Test"
DESCRIPTION = "QA Iotivity test which talks to the Simple Server example."
HOMEPAGE = "https://www.iotivity.org/"
DEPENDS = "iotivity"
SECTION = "apps"
LICENSE = "Apache-2.0"
LIC_FILES_CHKSUM = "file://servertest.cpp;beginline=1;endline=19;md5=fc5a615cf1dc3880967127bc853b3e0c"

SRC_URI = "file://iotivity-test.tar.gz \
          "

S = "${WORKDIR}/iotivity-test"

IOTIVITY_BIN_DIR = "/opt/iotivity-test"
IOTIVITY_BIN_DIR_D = "${D}${IOTIVITY_BIN_DIR}"

do_install() {
    install -d ${IOTIVITY_BIN_DIR_D}/apps/iotivity-test
    install -c -m 555 ${S}/output/clienttest ${IOTIVITY_BIN_DIR_D}/apps/iotivity-test
    install -c -m 555 ${S}/output/servertest ${IOTIVITY_BIN_DIR_D}/apps/iotivity-test
}

FILES_${PN} = "${IOTIVITY_BIN_DIR}/apps/iotivity-test/clienttest ${IOTIVITY_BIN_DIR}/apps/iotivity-test/servertest"
FILES_${PN}-dbg = "${IOTIVITY_BIN_DIR}/apps/iotivity-test/.debug"
RDEPENDS_${PN} += "iotivity"
BBCLASSEXTEND = "native nativesdk"

