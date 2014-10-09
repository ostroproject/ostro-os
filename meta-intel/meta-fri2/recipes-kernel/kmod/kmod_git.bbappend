do_install_append () {
	echo "blacklist gma500_gfx" > ${D}${sysconfdir}/modprobe.d/prohibit_gma500_gfx.conf
}
