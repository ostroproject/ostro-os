SUMMARY = "Set of files for testing losless compression algorithms"
DESCRIPTION = "Set of files for testing losless compression algorithms"
HOMEPAGE = "http://corpus.canterbury.ac.nz"
SECTION = "misc"
LICENSE = "GPLv2"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/GPL-2.0;md5=801f80980d171dd6425610833a22dbe6"

S = "${WORKDIR}/corpus"

SRC_URI = "http://corpus.canterbury.ac.nz/resources/calgary.tar.gz"

SRC_URI[md5sum] = "651d06b35d3d39522157cf8dc4a3d01c"
SRC_URI[sha256sum] = "e109eebdc19c5cee533c58bd6a49a4be3a77cc52f84ba234a089148a4f2093b7"

do_unpack () {
	mkdir -p ${S}
	tar -xf ${DL_DIR}/calgary.tar.gz -C ${WORKDIR}/corpus
}

FILES_${PN} = "/lib/firmware/*"

do_install () {
	install -d ${D}/lib/firmware
	install -m 664 ${S}/* ${D}/lib/firmware
}
