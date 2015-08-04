#
# Soletta image
#

SUMMARY = "A console-only image with built-in soletta"
LICENSE = "BSD"

IMAGE_INSTALL += "packagegroup-core-boot ${ROOTFS_PKGMANAGE_BOOTSTRAP} ${CORE_IMAGE_EXTRA_INSTALL} kernel-modules"

IMAGE_INSTALL += "soletta lss python3-jsonschema"

inherit core-image
