FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"
COMPATIBLE_MACHINE_emenlow = "emenlow"
KMACHINE_emenlow  = "emenlow"
KBRANCH_emenlow  = "yocto/standard/preempt-rt/base"

SRCREV_machine_pn-linux-yocto-rt_emenlow ?= ${AUTOREV}
SRCREV_meta_pn-linux-yocto-rt_emenlow ?= ${AUTOREV}
