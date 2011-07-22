FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"
COMPATIBLE_MACHINE_jasperforest = "jasperforest"
KMACHINE_jasperforest  = "jasperforest"
KBRANCH_jasperforest  = "yocto/standard/preempt-rt/base"

SRCREV_machine_pn-linux-yocto-rt_jasperforest ?= ${AUTOREV}
SRCREV_meta_pn-linux-yocto-rt_jasperforest ?= ${AUTOREV}
