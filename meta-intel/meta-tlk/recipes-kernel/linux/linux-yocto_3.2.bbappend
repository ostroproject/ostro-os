FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

# enable the time limited kernel configuration options
SRC_URI += "file://time-limited-kernel.cfg"

PR .= ".1"
