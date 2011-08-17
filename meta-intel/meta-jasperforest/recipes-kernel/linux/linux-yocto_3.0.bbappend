FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_jasperforest = "jasperforest"

KMACHINE_jasperforest  = "yocto/standard/common-pc-64/jasperforest"

SRCREV_machine_pn-linux-yocto_jasperforest ?= "48f6aaacf668d06aa9aba82501f31b3eff08df8d"
SRCREV_meta_pn-linux-yocto_jasperforest ?= "9da70812ecddee0f7eeb11675f29497cb997275e"
