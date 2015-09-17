# Upstream-Status: upstream has complete rewrite of the file in review

FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

SRC_URI_append = "\
     file://0001-sm130-remove-missing-return-value-from-SendCommand.patch \
"
