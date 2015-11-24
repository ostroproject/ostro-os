# include this file to customize standard Yocto images for edison

IMAGE_FEATURES += "debug-tweaks package-management ssh-server-openssh"

ROOTFS_POSTPROCESS_COMMAND += " edison_image_fixup ; "

edison_image_fixup() {

	cd ${IMAGE_ROOTFS}

	# add wpa_supplicant config for wlan0
	if [ -e etc/wpa_supplicant.conf ] ; then
		mkdir etc/wpa_supplicant
		cp etc/wpa_supplicant.conf etc/wpa_supplicant/wpa_supplicant-wlan0.conf
		ln -s /lib/systemd/system/wpa_supplicant@.service etc/systemd/system/multi-user.target.wants/wpa_supplicant@wlan0.service
		echo "[Match]"    >  etc/systemd/network/wlan0.network
		echo "Name=wlan0" >> etc/systemd/network/wlan0.network
		echo "[Network]"  >> etc/systemd/network/wlan0.network
		echo "DHCP=yes"   >> etc/systemd/network/wlan0.network
	fi
}

ROOTFS_POSTPROCESS_COMMAND =+ " add_custom_smart_config ; "

add_custom_smart_config() {

	if [ -d ${IMAGE_ROOTFS}/var/lib/smart ] ; then
		smart	--data-dir=${IMAGE_ROOTFS}/var/lib/smart channel \
			--add edison-all type=rpm-md name="Edison Package Repository (all)" \
			baseurl=${FEED_URL}/repo/rpm/all -y
		smart	--data-dir=${IMAGE_ROOTFS}/var/lib/smart channel \
			--add edison-core2-32 type=rpm-md name="Edison Package Repository (core2-32)" \
			baseurl=${FEED_URL}/repo/rpm/core2_32 -y
		smart	--data-dir=${IMAGE_ROOTFS}/var/lib/smart channel \
			--add edison-machine type=rpm-md name="Edison Package Repository (edison-machine)" \
			baseurl=${FEED_URL}/repo/rpm/edison -y
	fi
}
