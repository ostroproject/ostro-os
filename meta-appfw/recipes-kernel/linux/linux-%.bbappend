FILESEXTRAPATHS_prepend := "${THISDIR}/linux:"

# Kludge to reduce linux-% matching non-kernel packages to a no-op.
APP_FW_IS_KERNEL := "${@bb.data.inherits_class('kernel', d) and 'yes' or 'no'}"

# Our kernel configuration fragment (built-in overlayfs, {mac,ip}vlan, veth).
APP_FW_CFG_yes = "file://iot-app-fw.cfg"
APP_FW_CFG_no  = ""

SRC_URI_append = " ${APP_FW_CFG_${APP_FW_IS_KERNEL}}"
