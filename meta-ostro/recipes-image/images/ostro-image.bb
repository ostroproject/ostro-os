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
                packagegroup-core-connectivity \
                nodejs hid-api iotkit-agent upm tempered mraa linuxptp \
                iotivity-node iot-rest-api-server \
                packagegroup-user-management \
                iot-app-fw iot-app-fw-launcher \
                sensord \
                iproute2 \
                python-modules \
		"

IMAGE_FEATURES_append = " \
                        package-management \
                        ssh-server-dropbear \
                        "

# Use gummiboot as the EFI bootloader.
EFI_PROVIDER = "gummiboot"

# Install Cynara and security-manager by default if (and only if)
# Smack is enabled.
#
# Cynara does not have a hard dependency on Smack security,
# but is meant to be used with it. security-manager instead
# links against smack-userspace and expects Smack to be active,
# so we do not have any choice.
#
# Without configuration, security-manager is not usable. We use
# the policy packaged from the upstream source code here. Adapting
# it for the distro can be done by patching that source.
OSTRO_IMAGE_SECURITY_INSTALL_append_smack = "cynara security-manager security-manager-policy"
OSTRO_IMAGE_SECURITY_INSTALL ?= ""

IMAGE_LINGUAS = " "

LICENSE = "MIT"

inherit core-image extrausers image-buildinfo

# Set IMAGE_ROOTFS_EXTRA_SPACE to 512M (in Kbytes) to ensure there's
# always some extra space in the image.
IMAGE_ROOTFS_EXTRA_SPACE = "524288"

# Set root password to "ostro" if not set
OSTRO_ROOT_PASSWORD ?= "ostro"

def crypt_pass(d):
    import crypt, string, random
    character_set = string.letters + string.digits
    plaintext = d.getVar('OSTRO_ROOT_PASSWORD', True)

    if plaintext == "":
        return plaintext
    else:
        return crypt.crypt(plaintext, random.choice(character_set) + random.choice(character_set))

EXTRA_USERS_PARAMS = "\
usermod -p '${@crypt_pass(d)}' root; \
"

# Do not create ISO images by default, only HDDIMG will be created (if it gets created at all).
NOISO = "1"

# Replace the default "live" (aka HDDIMG) images with whole-disk images
# that contain multiple partitions (hdddirect = raw image, vdi/vmdk/qcow2 for
# different virtual machines). hdddirect is generated implicitly because the
# virtual image types depend on it. Only applicable to some machines.
OSTRO_VM_IMAGE_TYPES ?= "vdi vmdk qcow2"
IMAGE_FSTYPES_remove_intel-core2-32 = "live"
IMAGE_FSTYPES_append_intel-core2-32 = " ${OSTRO_VM_IMAGE_TYPES}"
IMAGE_FSTYPES_remove_intel-corei7-64 = "live"
IMAGE_FSTYPES_append_intel-corei7-64 = " ${OSTRO_VM_IMAGE_TYPES}"
IMAGE_FSTYPES_remove_intel-quark = "live"
IMAGE_FSTYPES_append_intel-quark = " ${OSTRO_VM_IMAGE_TYPES}"
# Remove also for qemu for the sake of consistency. It is not enabled there by default already.
IMAGE_FSTYPES_remove_qemux86 = "live"
IMAGE_FSTYPES_append_qemux86 = " ${OSTRO_VM_IMAGE_TYPES}"
IMAGE_FSTYPES_remove_qemux86-64 = "live"
IMAGE_FSTYPES_append_qemux86-64 = " ${OSTRO_VM_IMAGE_TYPES}"

# Inherit image-vm if any of the image fstypes depends on it.
# Works around an error from image.py:
# ERROR: No IMAGE_CMD defined for IMAGE_FSTYPES entry 'vdi' - possibly invalid type name or missing support class
# Necessary because the normal image class inheritance mechanism
# runs at the wrong time to avoid the image.py check.
inherit ${@'image-vm' if set(d.getVar('IMAGE_FSTYPES', True).split()).intersection(['vdi', 'vmdk', 'qcow2']) else ''}

BUILD_ID ?= "${DATETIME}"
IMAGE_BUILDINFO_VARS_append = " BUILD_ID"

IMAGE_NAME = "${IMAGE_BASENAME}-${MACHINE}-${BUILD_ID}"

# Enable initramfs based on initramfs-framework (chosen in
# core-image-minimal-initramfs.bbappend). All machines must
# boot with a suitable initramfs, because IMA initialization is done
# in it.
OSTRO_INITRAMFS ?= "ostro-initramfs"
INITRD_IMAGE_intel-core2-32 = "${OSTRO_INITRAMFS}"
INITRD_IMAGE_intel-corei7-64 = "${OSTRO_INITRAMFS}"
INITRD_IMAGE_intel-quark = "${OSTRO_INITRAMFS}"
INITRD_IMAGE_qemux86 = "${OSTRO_INITRAMFS}"
INITRD_IMAGE_qemux86-64 = "${OSTRO_INITRAMFS}"

# Our initramfs supports finding the partition by UUID, so use that
# to make the resulting whole-disk .hdddirect image more versatile (will
# work regardless whether the disk is attached via IDE, SATA, USB or
# copied to internal flash).
OSTRO_ROOT ?= "root=UUID=<<uuid-of-rootfs>>"
SYSLINUX_ROOT_intel-core2-32 = "${OSTRO_ROOT}"
SYSLINUX_ROOT_intel-corei7-64 = "${OSTRO_ROOT}"
SYSLINUX_ROOT_intel-quark = "${OSTRO_ROOT}"
SYSLINUX_ROOT_qemux86 = "${OSTRO_ROOT}"
SYSLINUX_ROOT_qemux86-64 = "${OSTRO_ROOT}"

# Activate IMA signing of rootfs, using the default (and insecure,
# because publicly available) keys shipped with the integrity
# layer. Actual products are expected to use their own, secret keys.
# See meta-integrity/README.md for the relevant configuration options.
#
# No IMA policy gets loaded, so in practice the resulting image runs
# without IMA.
inherit ima-evm-rootfs

# "evmctl ima_verify <file>" can be used to check that a file is
# really unmodified.
IMAGE_INSTALL += "ima-evm-utils"

# This limits attempts to mount the rootfs to exactly the right type.
# Avoids kernel messages like:
# EXT4-fs (hda2): couldn't mount as ext3 due to feature incompatibilities
# The VM types must be treated like ext4 (also hard-coded there).
APPEND_append = "${@''.join([' rootfstype=' + i for i in ['ext4', 'ext3', 'ext2'] if i in d.getVar('IMAGE_FSTYPES', True).replace('vdi', 'ext4').replace('vmdk', 'ext4').replace('qcow2', 'ext4').split()])}"

# Mount read-only at first. This gives systemd a chance to run fsck
# and then mount read/write.
APPEND_append = " ro"

# parted-native is required by wic to build the final image but has no
# explicit dependency set in recipes. Use EXTRA_IMAGEDEPENDS to ensure
# parted-native gets built.
EXTRA_IMAGEDEPENDS += "parted-native"

# Ensure that images preserve Smack labels and IMA/EVM.
inherit xattr-images
