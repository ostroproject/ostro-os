FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"
SRC_URI_append = " file://time-limited-kernel.cfg"
PR .= ".2"
