FILESEXTRAPATHS_prepend := "${THISDIR}/linux:"

IS_KERNEL_RECIPE := "${@bb.data.inherits_class('kernel', d) and 'yes' or 'no'}"

# Kernel config fragment enabling IMA/EVM
IMA_EVM_CFG_yes = " file://ima-evm.cfg"
IMA_EVM_CFG_no = ""
SRC_URI_append = "${IMA_EVM_CFG_${IS_KERNEL_RECIPE}}"

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
${do_compile_ima_evm_${IS_KERNEL_RECIPE}}
}
