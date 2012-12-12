FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

SRC_URI += "file://hdmi_port_audio.sh"

PR .= ".1"

do_install_append() {
	install -m 0755    ${WORKDIR}/hdmi_port_audio.sh       ${D}${sysconfdir}/init.d
	ln -sf          ../init.d/hdmi_port_audio.sh   ${D}${sysconfdir}/rcS.d/S66hdmi_port_audio.sh
}
