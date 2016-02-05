SUMMARY = "Checksec tool"
DESCRIPTION = "The checksec.sh script is designed to test what standard Linux OS and PaX security features are being used."
SECTION = "security"
LICENSE = "BSD-3-Clause"
HOMEPAGE="http://www.trapkit.de/tools/checksec.html"

LIC_FILES_CHKSUM = "file://checksec.sh;beginline=3;endline=34;md5=c1bd90129ce3bb5519cfcaea794ab515"

SRC_URI = "http://www.trapkit.de/tools/checksec.sh"

SRC_URI[md5sum] = "075996be339ab16ad7b94d6de3ee07bd"
SRC_URI[sha256sum] = "77b8a7fd9393d10def665658a41176ee745d5c7969a4a0f43cefcc8a4cd90947"

S = "${WORKDIR}"

do_install() {
    install -d ${D}${bindir}
    install -m 0755 ${WORKDIR}/checksec.sh    ${D}${bindir}
}

RDEPENDS_${PN} = "bash binutils"

BBCLASSEXTEND = "native"
