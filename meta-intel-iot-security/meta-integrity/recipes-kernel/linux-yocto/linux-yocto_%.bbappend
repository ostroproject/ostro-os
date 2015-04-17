FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

# Kernel config fragment enabling IMA/EVM
SRC_URI_append = " file://ima-evm.cfg"

do_compile_prepend () {
    # Put our x509 file into the build directory where the kernel
    # compilation will find it automatically. We use the build
    # directory because the source might be shared with
    # other builds where we do not want this key.
    #
    # The IMA_EVM_ROOT_CA default is set globally in ima-evm-rootfs.bbclass.
    [ "${IMA_EVM_ROOT_CA}" ] && cp "${IMA_EVM_ROOT_CA}" "${B}"
}
