# Update the init script for the tiny image to manually mount devtmpfs and
# ensure the ttyPCH1 device is available for the console.

FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"
 
PRINC := "${@int(PRINC) + 1}"
