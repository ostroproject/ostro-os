FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"
COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2 = "fri2"
KBRANCH_fri2 = "yocto/standard/preempt-rt/base"

SRCREV_machine_pn-linux-yocto-rt_fri2 ?= ${AUTOREV}
SRCREV_meta_pn-linux-yocto-rt_fri2 ?= ${AUTOREV}
