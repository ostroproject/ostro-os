FILESEXTRAPATHS_prepend := "${THISDIR}/base-files:"

SRC_URI += "file://factory.mount"
SRC_URI += "file://fstab"

# override default volatile to suppress var/log link creation
volatiles = "tmp"

do_install_append() {
	install -d ${D}${sysconfdir}
	install -m 0644 ${WORKDIR}/fstab ${D}${sysconfdir}/fstab

	install -d ${D}${systemd_unitdir}/system
	install -c -m 0644 ${WORKDIR}/factory.mount ${D}${systemd_unitdir}/system

	# Enable the service
	install -d ${D}${sysconfdir}/systemd/system/default.target.wants
	ln -sf ${systemd_unitdir}/system/factory.mount \
		${D}${sysconfdir}/systemd/system/default.target.wants/factory.mount

}

FILES_${PN} += "${base_libdir}/systemd/system/*.mount"
FILES_${PN} += "${sysconfdir}/systemd/system/default.target.wants/*.mount"

