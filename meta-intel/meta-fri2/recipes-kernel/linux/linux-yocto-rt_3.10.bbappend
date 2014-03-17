FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2 = "fri2"
KBRANCH_fri2 = "standard/preempt-rt/fri2"
SRCREV_machine_pn-linux-yocto-rt_fri2 ?= "6df6580e4a54308346d4ebaaa433932842ac8783"
#SRCREV_meta_pn-linux-yocto-rt_fri2 ?= "XXX"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
KBRANCH_fri2-noemgd = "standard/preempt-rt/fri2"
SRCREV_machine_pn-linux-yocto-rt_fri2-noemgd ?= "6df6580e4a54308346d4ebaaa433932842ac8783"
#SRCREV_meta_pn-linux-yocto-rt_fri2-noemgd ?= "XXX"

module_autoload_iwlwifi = "iwlwifi"
