FILESEXTRAPATHS_prepend_edison := "${THISDIR}/base-files:"

SRC_URI_append_edison = " file://factory.mount"
SRC_URI_append_edison = " file://fstab"

# override default volatile to suppress var/log link creation
volatiles_edison = "tmp"

do_install_append_edison() {
	install -d ${D}${sysconfdir}
	install -m 0644 ${WORKDIR}/fstab ${D}${sysconfdir}/fstab

	install -d ${D}${systemd_unitdir}/system
	install -c -m 0644 ${WORKDIR}/factory.mount ${D}${systemd_unitdir}/system

	# Enable the service
	install -d ${D}${sysconfdir}/systemd/system/default.target.wants
	ln -sf ${systemd_unitdir}/system/factory.mount \
		${D}${sysconfdir}/systemd/system/default.target.wants/factory.mount

}

FILES_${PN}_append_edison = " ${base_libdir}/systemd/system/*.mount"
FILES_${PN}_append_edison = " ${sysconfdir}/systemd/system/default.target.wants/*.mount"

