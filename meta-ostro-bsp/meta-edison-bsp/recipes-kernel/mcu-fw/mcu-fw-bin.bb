DESCRIPTION = "This is edison mcu fw binary."
HOMEPAGE = "http://www.intel.com"
LICENSE = "CLOSED"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

SRC_URI = "file://intel_mcu.bin"

S = "${WORKDIR}"

do_install () {
	install -v -d ${D}/${base_libdir}/firmware/
	install -m 644 intel_mcu.bin ${D}/${base_libdir}/firmware/
}

FILES_${PN} = "${base_libdir}/firmware/"

