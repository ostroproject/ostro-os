SUMMARY = "Intel Quick Assist Driver - Canterbury Corpus"
DESCRIPTION = "Set of files for testing losless compression algorithms \
		for Intel Crystal Forest BSP Quick Assist Technology Software Package"

HOMEPAGE = "http://corpus.canterbury.ac.nz"
SECTION = "misc"
LICENSE = "GPLv2"

LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/GPL-2.0;md5=801f80980d171dd6425610833a22dbe6"

PR = "r0"

S = "${WORKDIR}/canterbury-corpus"

SRC_URI = "http://corpus.canterbury.ac.nz/resources/cantrbry.tar.gz"

SRC_URI[md5sum] = "442e56cfffdf460d25b0b91650a55908"
SRC_URI[sha256sum] = "f140e8a5b73d3f53198555a63bfb827889394a42f20825df33c810c3d5e3f8fb"

# Disable architecture QA check for this package since it contains
# pre-compiled executable "sum" for SPARC. The package is used
# for compression benchmarking only.
WARN_QA += ""
ERROR_QA = ""

do_package_qa[noexec] = "1"

do_unpack () {
	mkdir -p ${S}
	tar -xf ${DL_DIR}/cantrbry.tar.gz -C ${S}
}

do_unpack_append () {
	rm -rf ${S}/patches
}

FILES_${PN} = "/lib/firmware/*"

do_install () {
	install -d ${D}${base_libdir}/firmware
	install -m 644 ${S}/* ${D}${base_libdir}/firmware
}
