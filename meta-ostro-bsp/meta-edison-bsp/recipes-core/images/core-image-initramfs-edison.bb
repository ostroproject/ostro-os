# Simple initramfs image.
DESCRIPTION = "Small initramfs image capable of supporting fota."

PACKAGE_INSTALL = "initramfs-boot ${VIRTUAL-RUNTIME_base-utils} udev base-passwd u-boot-fw-utils-edison dosfstools e2fsprogs-mke2fs e2fsprogs-tune2fs ${ROOTFS_BOOTSTRAP_INSTALL} watchdog"

# Do not pollute the initrd image with rootfs features
IMAGE_FEATURES = ""

export IMAGE_BASENAME = "core-image-initramfs-edison"
IMAGE_LINGUAS = ""

LICENSE = "MIT"

#EXTRA_IMAGECMD = "-O ^sparse_super2"
IMAGE_FSTYPES = "${INITRAMFS_FSTYPES}"
inherit core-image

IMAGE_ROOTFS_SIZE = "8192"

BAD_RECOMMENDATIONS += "busybox-syslog systemd"

USE_DEVFS = "0"

