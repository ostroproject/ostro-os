# Simple initramfs image.
DESCRIPTION = "Small initramfs image capable of supporting fota."

PACKAGE_INSTALL = "initramfs-boot busybox udev base-passwd u-boot-fw-utils dosfstools e2fsprogs-mke2fs e2fsprogs-tune2fs ${ROOTFS_BOOTSTRAP_INSTALL}"

# Do not pollute the initrd image with rootfs features
IMAGE_FEATURES = ""

IMAGE_LINGUAS = ""

LICENSE = "MIT"

IMAGE_FSTYPES = "${INITRAMFS_FSTYPES}"
inherit core-image

IMAGE_ROOTFS_SIZE = "8192"

BAD_RECOMMENDATIONS += "busybox-syslog systemd"

USE_DEVFS = "0"

