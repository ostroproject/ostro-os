FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

# Kernel config fragment enabling IMA/EVM
SRC_URI_append = " file://ima-evm.cfg"
