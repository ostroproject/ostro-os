# Upstream-Status: Submitted

FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

SRC_URI_append = "\ 
     file://0001-mke2fs-check-string-lengths-before-strncpy.patch \
"
