FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_jasperforest = "jasperforest"

KMACHINE_jasperforest  = "yocto/standard/common-pc-64/jasperforest"

SRCREV_machine_pn-linux-yocto_jasperforest ?= "8cc4724f41f9082e48e5a846a29f6f6356c16b61"
SRCREV_meta_pn-linux-yocto_jasperforest ?= "d5d3c6480d61f83503ccef7fbcd765f7aca8b71b"
