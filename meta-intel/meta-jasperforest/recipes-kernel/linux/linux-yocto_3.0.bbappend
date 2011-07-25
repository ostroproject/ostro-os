FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_jasperforest = "jasperforest"

KMACHINE_jasperforest  = "yocto/standard/common-pc-64/jasperforest"

SRCREV_machine_pn-linux-yocto_jasperforest ?= "3216e7d5c3cada16161481826cdb39c930457587"
SRCREV_meta_pn-linux-yocto_jasperforest ?= "9010d1cbef2633dac7e559a7705c326b7601dd4c"
