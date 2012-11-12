FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow = "emenlow"
KMACHINE_emenlow  = "emenlow"
KBRANCH_emenlow  = "standard/emenlow"

SRCREV_machine_pn-linux-yocto_emenlow ?= "${AUTOREV}"
SRCREV_meta_pn-linux-yocto_emenlow ?= "${AUTOREV}"
