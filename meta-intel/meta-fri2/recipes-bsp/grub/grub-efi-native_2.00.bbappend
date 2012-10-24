# The Intel provided Fast Boot Firmware may not initialize the USB keyboard
# before launching the grub.efi payload. Ensure GRUB has keyboard control by
# building in the usb, usb_keyboard, and ohci modules.

do_mkimage() {
	./grub-mkimage -p /EFI/BOOT -d ./grub-core/ \
	               -O ${GRUB_TARGET}-efi -o ./${GRUB_IMAGE} \
	               boot linux ext2 fat serial part_msdos part_gpt normal efi_gop \
	               usb usb_keyboard ohci
}

