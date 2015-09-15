FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

SRC_URI_append_edison = " file://systemd-enable-watchdog.patch"
SRC_URI_append_beaglebone = " file://systemd-enable-watchdog.patch"
SRC_URI_append_intel-corei7-64 = " file://systemd-enable-watchdog.patch"
