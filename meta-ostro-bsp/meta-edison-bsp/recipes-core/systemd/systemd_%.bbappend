FILESEXTRAPATHS_prepend_edison := "${THISDIR}/files:"

SRC_URI_append_edison = " file://wlan0.network"

FILES_${PN} += "${sysconfdir}/systemd/network"

do_install_append_edison () {
	install -m 755 -d ${D}${sysconfdir}/systemd/network
	install -m 644 ${WORKDIR}/wlan0.network ${D}${sysconfdir}/systemd/network/
}
