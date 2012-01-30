FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_jasperforest = "jasperforest"

KMACHINE_jasperforest  = "yocto/standard/common-pc-64/jasperforest"

SRCREV_machine_pn-linux-yocto_jasperforest ?= "fc10a49bed173ade9c6c076241a448639fe50aa8"
SRCREV_meta_pn-linux-yocto_jasperforest ?= "59314a3523e360796419d76d78c6f7d8c5ef2593"
