# The Intel provided Fast Boot Firmware may not initialize the USB keyboard
# before launching the grub.efi payload. Ensure GRUB has keyboard control by
# building in the usb, usb_keyboard, and ohci modules.

do_deploy() {
	# Search for the grub.cfg on the local boot media by using the
	# built in cfg file provided via this recipe
	grub-mkimage -c ../cfg -p /EFI/BOOT -d ./grub-core/ \
	               -O ${GRUB_TARGET}-efi -o ./${GRUB_IMAGE} \
	               boot linux ext2 fat serial part_msdos part_gpt normal efi_gop iso9660 search \
	               usb usb_keyboard ohci
	install -m 644 ${B}/${GRUB_IMAGE} ${DEPLOYDIR}
}
