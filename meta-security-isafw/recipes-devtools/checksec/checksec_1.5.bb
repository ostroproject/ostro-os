SUMMARY = "Checksec tool"
DESCRIPTION = "The checksec.sh script is designed to test what standard Linux OS and PaX security features are being used."
SECTION = "security"
LICENSE = "BSD-3-Clause"
HOMEPAGE="http://www.trapkit.de/tools/checksec.html"

LIC_FILES_CHKSUM = "file://checksec.sh;beginline=3;endline=34;md5=c1bd90129ce3bb5519cfcaea794ab515"

SRC_URI = "file://checksec.sh"

S = "${WORKDIR}"

do_install() {
    install -d ${D}${bindir}
    install -m 0755 ${WORKDIR}/checksec.sh    ${D}${bindir}
}

RDEPENDS_${PN} = "bash binutils"

BBCLASSEXTEND = "native"
