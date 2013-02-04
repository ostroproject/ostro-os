FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_jasperforest = "jasperforest"

KMACHINE_jasperforest  = "jasperforest"
KBRANCH_jasperforest  = "standard/default/common-pc-64/jasperforest"

SRCREV_machine_pn-linux-yocto_jasperforest ?= "2a98cc74757bd353c7d49a2d0c7b479aba81d58e"
SRCREV_meta_pn-linux-yocto_jasperforest ?= "e7f2fdc48f8808887175f0328274a2668084738c"

LINUX_VERSION = "3.2.32"
