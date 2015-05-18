FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

# Kernel config fragment enabling Smack, without making it the default explicitly.
SRC_URI_append_smack = " file://smack.cfg"

# When added, set Smack as the default LSM.
SMACK_DEFAULT_SECURITY_CFG = "file://smack-default-lsm.cfg"

# Add it by default, can be overridden by changing this variable here.
SMACK_DEFAULT_SECURITY ??= "${SMACK_DEFAULT_SECURITY_CFG}"
SRC_URI_append_smack = " ${SMACK_DEFAULT_SECURITY}"
