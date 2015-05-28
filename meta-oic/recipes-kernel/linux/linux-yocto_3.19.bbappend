FILESEXTRAPATHS_prepend := "${THISDIR}/files:"

#
# Add default bluetooth kernel feature
#
KERNEL_FEATURES += " features/bluetooth/bluetooth.scc"

#
# specifying additional kernel feature
#
SRC_URI += "file://bluetooth.cfg"

