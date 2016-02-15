FILESEXTRAPATHS_prepend := "${THISDIR}/linux:"

IS_KERNEL_RECIPE := "${@bb.data.inherits_class('kernel', d) and 'yes' or 'no'}"
SMACK_KERNEL_SRC_URI_no = ""
SMACK_KERNEL_SRC_URI_yes = ""

# Kernel config fragment enabling Smack, without making it the default explicitly.
SMACK_KERNEL_SRC_URI_yes += "file://smack.cfg"

# When added, set Smack as the default LSM.
SMACK_DEFAULT_SECURITY_CFG = "file://smack-default-lsm.cfg"

# Add it by default, can be overridden by changing this variable here.
SMACK_DEFAULT_SECURITY ??= "${SMACK_DEFAULT_SECURITY_CFG}"
SMACK_KERNEL_SRC_URI_yes += " ${SMACK_DEFAULT_SECURITY}"

SRC_URI_append_smack = "${SMACK_KERNEL_SRC_URI_${IS_KERNEL_RECIPE}}"
