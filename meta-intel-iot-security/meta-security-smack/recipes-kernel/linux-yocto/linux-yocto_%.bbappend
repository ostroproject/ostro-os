FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

# Kernel config fragment enabling Smack.
SRC_URI_append_smack = " file://smack.cfg"
