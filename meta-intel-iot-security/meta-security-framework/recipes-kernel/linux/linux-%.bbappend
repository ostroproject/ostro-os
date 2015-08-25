# Enables finding the audit.cfg. Could be made conditional
# on a new distro feature, but for now activate it via local.conf
# with:
#    SRC_URI_append_pn-linux-yocto = " file://audit.cfg"
#
# Replace linux-yocto with your actual kernel recipe name if
# different.

FILESEXTRAPATHS_prepend := "${THISDIR}/linux:"
