# Upstream-Status: Accepted

FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

SRC_URI_append = "\ 
     file://0001-fix-possible-uninitialized-array-values.patch \
     file://0002-fix-possible-resource-leak-with-yynultrans_tbl.patch \
"
