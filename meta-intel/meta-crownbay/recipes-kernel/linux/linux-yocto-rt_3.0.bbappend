FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"
COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd = "crownbay"
KBRANCH_crownbay-noemgd = "yocto/standard/preempt-rt/base"

KERNEL_FEATURES_append_crownbay-noemgd += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto-rt_crownbay-noemgd ?= ${AUTOREV}
SRCREV_meta_pn-linux-yocto-rt_crownbay-noemgd ?= ${AUTOREV}
