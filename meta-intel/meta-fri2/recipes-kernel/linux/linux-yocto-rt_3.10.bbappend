FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2 = "fri2"
KBRANCH_fri2 = "standard/preempt-rt/fri2"
SRCREV_machine_pn-linux-yocto-rt_fri2 ?= "b669af08737562ef86e7cba328966d05222d3e64"
#SRCREV_meta_pn-linux-yocto-rt_fri2 ?= "XXX"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
KBRANCH_fri2-noemgd = "standard/preempt-rt/fri2"
SRCREV_machine_pn-linux-yocto-rt_fri2-noemgd ?= "b669af08737562ef86e7cba328966d05222d3e64"
#SRCREV_meta_pn-linux-yocto-rt_fri2-noemgd ?= "XXX"

KERNEL_MODULE_AUTOLOAD += "iwlwifi"
