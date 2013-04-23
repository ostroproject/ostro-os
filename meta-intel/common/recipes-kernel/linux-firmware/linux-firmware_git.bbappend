FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"
PRINC := "${@int(PRINC) + 1}"

# This exists in Yocto 1.1, but include it here for completeness
LIC_FILES_CHKSUM += "file://LICENCE.iwlwifi_firmware;md5=11545778abf78c43d7644d4f171ea1c7"

FWPATH = "/lib/firmware"

do_install_append() {
	install -m 0644 LICENCE.iwlwifi_firmware ${D}${FWPATH}
	install -m 0644 iwlwifi-6000g2a-5.ucode ${D}${FWPATH}
	install -m 0644 iwlwifi-6000g2b-6.ucode ${D}${FWPATH}
}

PACKAGES =+ "${PN}-iwlwifi-licence \
             ${PN}-iwlwifi-6000g2a-5 \
             ${PN}-iwlwifi-6000g2b-6"

RDEPENDS_${PN}-iwlwifi-6000g2a-5 = "${PN}-iwlwifi-licence"
RDEPENDS_${PN}-iwlwifi-6000g2b-6 = "${PN}-iwlwifi-licence"

FILES_${PN}-iwlwifi-licence =   "${FWPATH}/LICENCE.iwlwifi_firmware"
FILES_${PN}-rtl-license =       "${FWPATH}/LICENCE.rtlwifi_firmware.txt"
FILES_${PN}-iwlwifi-6000g2a-5 = "${FWPATH}/iwlwifi-6000g2a-5.ucode"
FILES_${PN}-iwlwifi-6000g2b-6 = "${FWPATH}/iwlwifi-6000g2b-6.ucode"
