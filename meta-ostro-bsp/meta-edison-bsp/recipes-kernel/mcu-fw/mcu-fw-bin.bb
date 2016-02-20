DESCRIPTION = "This is edison mcu fw binary."
HOMEPAGE = "http://www.intel.com"

LICENSE = "Intel-OBL-Binary-Firmware-License"
LIC_FILES_CHKSUM = "file://LICENSE;md5=41b172554812bbdd8ef5b0711639b69b"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

SRC_URI = "file://intel_mcu.bin \
           file://LICENSE"

S = "${WORKDIR}"

do_install () {
	install -v -d ${D}/${base_libdir}/firmware/
	install -m 644 intel_mcu.bin ${D}/${base_libdir}/firmware/
}

FILES_${PN} = "${base_libdir}/firmware/"

