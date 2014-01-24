FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

PACKAGE_ARCH_jasperforest = "${MACHINE_ARCH}"

COMPATIBLE_MACHINE_jasperforest = "jasperforest"

KMACHINE_jasperforest  = "jasperforest"
KBRANCH_jasperforest  = "standard/common-pc-64/jasperforest"

SRCREV_machine_pn-linux-yocto_jasperforest ?= "de0c0ed674dfdbd808657e299fc720d8a97cb868"
SRCREV_meta_pn-linux-yocto_jasperforest ?= "9473a39c59bf9c07a316486d272652bacb9ad3ac"

LINUX_VERSION = "3.4.46"
