IMA_ENABLED_HERE := "${@'yes' if bb.data.inherits_class('kernel', d) and 'ima' in d.getVar('DISTRO_FEATURES', True).split() else 'no'}"

IMA_FILESEXTRAPATHS_yes := "${THISDIR}/linux:"
IMA_FILESEXTRAPATHS_no := ""
FILESEXTRAPATHS_prepend := "${IMA_FILESEXTRAPATHS_${IMA_ENABLED_HERE}}"

# Kernel config fragment enabling IMA/EVM
IMA_EVM_CFG_yes = " file://ima.cfg"
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
