SUMMARY = "Ostro OS Image."

IMAGE_INSTALL = " \
		kernel-modules \
		linux-firmware \
		packagegroup-core-boot \
                ${ROOTFS_PKGMANAGE_BOOTSTRAP} \
                ${CORE_IMAGE_EXTRA_INSTALL} \
                ${OSTRO_IMAGE_SECURITY_INSTALL} \
                iotivity iotivity-simple-client \
                iotivity-resource iotivity-resource-samples \
                nodejs hid-api iotkit-agent upm tempered mraa linuxptp \
		"

# Cynara does not have a hard dependency on Smack security,
# but is meant to be used with it. security-manager even
# links against smack-userspace. So only install them by
# default when Smack is enabled.
OSTRO_IMAGE_SECURITY_INSTALL_append_smack = "cynara security-manager"
OSTRO_IMAGE_SECURITY_INSTALL ?= ""

IMAGE_LINGUAS = " "

LICENSE = "MIT"

inherit core-image

IMAGE_ROOTFS_SIZE ?= "8192"
