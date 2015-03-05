FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

# Kernel config fragment enabling Smack.
SRC_URI += "file://smack.cfg"
