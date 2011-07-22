FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"
COMPATIBLE_MACHINE_n450 = "n450"
KMACHINE_n450 = "atom-pc"
KBRANCH_n450 = "yocto/standard/preempt-rt/base"

KERNEL_FEATURES_append_n450 += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto-rt_n450 ?= ${AUTOREV}
SRCREV_meta_pn-linux-yocto-rt_n450 ?= ${AUTOREV}
