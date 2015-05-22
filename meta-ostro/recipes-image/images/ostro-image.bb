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
OSTRO_IMAGE_SECURITY_INSTALL_append_smack = "cynara security-manager"
OSTRO_IMAGE_SECURITY_INSTALL ?= ""

IMAGE_LINGUAS = " "

LICENSE = "MIT"

inherit core-image extrausers

IMAGE_ROOTFS_SIZE ?= "8192"

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

# Do not create ISO images by default, only HDDIMG will be created
NOISO = "1"
