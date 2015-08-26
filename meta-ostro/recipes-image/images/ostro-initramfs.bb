# Ostro OS initramfs image. Derived from core-image-minimal-initramfs,
# with initramfs-framework instead of initramfs-live-boot and
# initramfs-live-install.
#
# Debugging tips for local.conf:
# SYSLINUX_PROMPT = "100" - show menu for 10 seconds
# AUTO_SYSLINUXMENU = "1" - automatically generate menu with choice between graphics and serial boot
# SYSLINUX_TIMEOUT = "100" - boot after waiting for 10 seconds

DESCRIPTION = "Small image capable of booting a device. The kernel includes \
the Minimal RAM-based Initial Root Filesystem (initramfs), which finds the \
first 'init' program more efficiently."

PACKAGE_INSTALL = "busybox base-passwd ${ROOTFS_BOOTSTRAP_INSTALL}"

# e2fs: loads fs modules and adds ext2/ext3/ext4=<device>:<path> boot parameter
#       for mounting additional partitions

# used to detect boot devices automatically
PACKAGE_INSTALL += "initramfs-module-udev"

# debug: adds debug boot parameters like 'shell' and 'debug', see
#        meta/recipes-core/initrdscripts/initramfs-framework/debug for details
# Could be removed in more minimal product image.
PACKAGE_INSTALL += "initramfs-module-debug"

# Do not pollute the initrd image with rootfs features
IMAGE_FEATURES = ""

export IMAGE_BASENAME = "ostro-initramfs"
IMAGE_LINGUAS = ""

LICENSE = "MIT"

IMAGE_FSTYPES = "${INITRAMFS_FSTYPES}"
inherit core-image

BAD_RECOMMENDATIONS += "busybox-syslog"
