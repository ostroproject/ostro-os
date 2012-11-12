FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_jasperforest = "jasperforest"

KMACHINE_jasperforest  = "jasperforest"
KBRANCH_jasperforest  = "standard/common-pc-64/jasperforest"

SRCREV_machine_pn-linux-yocto_jasperforest ?= "${AUTOREV}"
SRCREV_meta_pn-linux-yocto_jasperforest ?= "${AUTOREV}"
