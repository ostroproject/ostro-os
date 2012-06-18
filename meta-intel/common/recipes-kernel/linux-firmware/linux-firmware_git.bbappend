FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

# This exists in Yocto 1.1, but include it here for completeness
LIC_FILES_CHKSUM += "file://LICENCE.iwlwifi_firmware;md5=311cc823df5b1be4f00fbf0f17d96a6b"

FWPATH = "/lib/firmware"

do_install_append() {
	install -m 0644 LICENCE.iwlwifi_firmware ${D}${FWPATH}
	install -m 0644 iwlwifi-6000g2a-5.ucode ${D}${FWPATH}
}

PACKAGES =+ "${PN}-iwlwifi-6000g2a-5"

FILES_${PN}-iwlwifi-6000g2a-5 = "  \
  ${FWPATH}/LICENCE.iwlwifi_firmware \
  ${FWPATH}/iwlwifi-6000g2a-5.ucode  \
"
