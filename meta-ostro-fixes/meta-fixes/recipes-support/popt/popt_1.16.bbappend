# Upstream-Status: fixed in upstream head

FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

SRC_URI_append = "\ 
     file://0001-poptint.c-fix-possible-resource-leak.patch \
     file://0002-poptconfig.c-fix-possible-resource-leak.patch \
 \
"
