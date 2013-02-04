FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_jasperforest = "jasperforest"

KMACHINE_jasperforest  = "jasperforest"
KBRANCH_jasperforest  = "standard/common-pc-64/jasperforest"

SRCREV_machine_pn-linux-yocto_jasperforest ?= "13809f2cfd9be0ce86bd486e1643f9b90bed6f4f"
SRCREV_meta_pn-linux-yocto_jasperforest ?= "f697e099bc76d5df3a307a5bc0cc25021dd6dfe0"

LINUX_VERSION = "3.4.28"
