DESCRIPTION = "This is intel mcu app download daemon."
HOMEPAGE = "http://www.intel.com"
LICENSE = "CLOSED"

FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"

SRC_URI = "file://mcu_fw_loader.service \
		   file://mcu_fw_loader.sh"

SYSTEMD_SERVICE_${PN} = "mcu_fw_loader.service"

S = "${WORKDIR}"

inherit systemd

do_install () {
	install -d ${D}${sysconfdir}/intel_mcu/
	install -m 0755 mcu_fw_loader.sh ${D}${sysconfdir}/intel_mcu/

	install -d ${D}${systemd_unitdir}/system/
	install -m 0644 mcu_fw_loader.service ${D}${systemd_unitdir}/system/
}

