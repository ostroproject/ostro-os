IMA_ENABLED_HERE := "${@'yes' if bb.data.inherits_class('kernel', d) and 'ima' in d.getVar('DISTRO_FEATURES', True).split() else 'no'}"

IMA_FILESEXTRAPATHS_yes := "${THISDIR}/linux:"
IMA_FILESEXTRAPATHS_no := ""
FILESEXTRAPATHS_prepend := "${IMA_FILESEXTRAPATHS_${IMA_ENABLED_HERE}}"

# These two patches are necessary to unpack archives with security.ima xattr
# such that security.ima is taken from the archive. If the policy
# allows hashing, unpatched kernels (at least up to 4.3) will replace
# a signed hash in security.ima with a locally computed hash.
#
# Note that only bsdtar/libarchive are known to work; GNU tar sets
# the security.ima on an empty file and the tries re-opening it for
# writing its content, which then fails due to the IMA hash mismatch.
#
# Kernels >= 4.7 have the patches, while older kernels are likely to
# need the patches. So apply them by default. To avoid that,
# set IMA_EVM_SETATTR_PATCH_x.y.z (where x.y.z == linux kernel version)
# to an empty string (to avoid patching) or some other patch files
# suitable for that kernel.
def ima_evm_setattr_patch(d):
    result = []
    linux_version = d.getVar('LINUX_VERSION', True) or ''
    # These two patches are known to be included upstream.
    if bb.utils.vercmp_string_op(linux_version, '4.7', '<'):
        patches = d.getVar('IMA_EVM_SETATTR_PATCH_' + linux_version, True)
        if patches != None:
            # Patches explicitly chosen, may be empty.
            result.append(patches)
        else:
            # Enabled by default.
            result.append('file://0001-ima-fix-ima_inode_post_setattr.patch file://0002-ima-add-support-for-creating-files-using-the-mknodat.patch')
    # This one addresses a problem added in 4.2. The upstream revert will land
    # in some future kernel. We need to extend version check once we know
    # which kernels have the patch.
    if bb.utils.vercmp_string_op(linux_version, '4.2', '>='):
        patches = d.getVar('IMA_EVM_SETATTR_REVERT_PATCH_' + linux_version, True)
        if patches != None:
            # Patches explicitly chosen, may be empty.
            result.append(patches)
        else:
            # Enabled by default.
            result.append('file://Revert-ima-limit-file-hash-setting-by-user-to-fix-an.patch')
    return ' '.join(result)

# Edison kernel too old, patch not applicable -> swupd is broken in Ostro OS for Edison.
IMA_EVM_SETATTR_PATCH_3.10.98 = ""

# Kernel config fragment enabling IMA/EVM and (where necessary and possible)
# also patching the kernel.
IMA_EVM_CFG_yes = " file://ima.cfg \
                    ${@ ima_evm_setattr_patch(d)} \
                  "
IMA_EVM_CFG_no = ""
SRC_URI_append = "${IMA_EVM_CFG_${IMA_ENABLED_HERE}}"

# Put our x509 file into the build directory where the kernel
# compilation will find it automatically. We use the build
# directory because the source might be shared with
# other builds where we do not want this key.
#
# The IMA_EVM_ROOT_CA default is set globally in ima-evm-rootfs.bbclass.
# Need weaker default here in case that ima-evm-rootfs.bbclass is not
# inherited.
IMA_EVM_ROOT_CA ??= ""
do_compile_ima_evm_yes = "    [ '${IMA_EVM_ROOT_CA}' ] && cp '${IMA_EVM_ROOT_CA}' '${B}'"
do_compile_ima_evm_no = ":"

do_compile_prepend () {
${do_compile_ima_evm_${IMA_ENABLED_HERE}}
}
