# Upstream-Status: merged to upstream master

FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

SRC_URI_append = "\ 
     file://0001-getfacl-Fix-minor-resource-leak.patch \
"
