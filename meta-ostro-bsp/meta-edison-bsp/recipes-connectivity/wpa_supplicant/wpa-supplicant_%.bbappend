do_install_append_edison () {
	install -d ${D}${sysconfdir}/wpa_supplicant
	install -m 600 ${WORKDIR}/wpa_supplicant.conf-sane ${D}${sysconfdir}/wpa_supplicant/wpa_supplicant-wlan0.conf

	if ${@bb.utils.contains('DISTRO_FEATURES','systemd','true','false',d)}; then
		install -d ${D}${sysconfdir}/systemd/system/multi-user.target.wants
		ln -s ${base_libdir}/systemd/system/wpa_supplicant@.service ${D}${sysconfdir}/systemd/system/multi-user.target.wants/wpa_supplicant@wlan0.service
	fi
}
