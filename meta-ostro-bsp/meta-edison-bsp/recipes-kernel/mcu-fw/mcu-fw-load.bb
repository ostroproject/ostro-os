DESCRIPTION = "This is intel mcu app download daemon."
HOMEPAGE = "http://www.intel.com"

LICENSE = "Intel-OBL-Binary-Firmware-License"
LIC_FILES_CHKSUM = "file://LICENSE;md5=41b172554812bbdd8ef5b0711639b69b"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

SRC_URI = "file://mcu_fw_loader.service \
           file://mcu_fw_loader.sh \
           file://LICENSE"

SYSTEMD_SERVICE_${PN} = "mcu_fw_loader.service"

S = "${WORKDIR}"

inherit systemd

do_install () {
	install -d ${D}${sysconfdir}/intel_mcu/
	install -m 0755 mcu_fw_loader.sh ${D}${sysconfdir}/intel_mcu/

	install -d ${D}${systemd_unitdir}/system/
	install -m 0644 mcu_fw_loader.service ${D}${systemd_unitdir}/system/
}

