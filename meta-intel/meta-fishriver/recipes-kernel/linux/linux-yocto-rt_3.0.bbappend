FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"
COMPATIBLE_MACHINE_fishriver = "fishriver"
KMACHINE_fishriver  = "fishriver"
KBRANCH_fishriver  = "yocto/standard/preempt-rt/base"

SRCREV_machine_pn-linux-yocto-rt_fishriver ?= ${AUTOREV}
SRCREV_meta_pn-linux-yocto-rt_fishriver ?= ${AUTOREV}
