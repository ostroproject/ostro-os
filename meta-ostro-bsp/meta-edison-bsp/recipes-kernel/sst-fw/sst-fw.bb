DESCRIPTION = "Edison sst fw binary."
HOMEPAGE = "http://www.intel.com"
LICENSE = "CLOSED"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

SRC_URI = "file://fw_sst_119a.bin"

S = "${WORKDIR}"

do_install () {
    install -v -d ${D}/${base_libdir}/firmware/
    install -m 644 fw_sst_119a.bin ${D}/${base_libdir}/firmware/
}

INSANE_SKIP_${PN} = "arch"

FILES_${PN} = "${base_libdir}/firmware/"

