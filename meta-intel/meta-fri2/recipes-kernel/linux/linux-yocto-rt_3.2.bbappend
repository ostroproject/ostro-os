FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2 = "fri2"
#KBRANCH_fri2 = "standard/preempt-rt/base"
SRCREV_machine_pn-linux-yocto-rt_fri2 ?= "fe2630b38159ea7b9cf977b5fed40a9917002087"
SRCREV_meta_pn-linux-yocto-rt_fri2 ?= "5b4c9dc78b5ae607173cc3ddab9bce1b5f78129b"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
#KBRANCH_fri2-noemgd = "standard/preempt-rt/base"
SRCREV_machine_pn-linux-yocto-rt_fri2-noemgd ?= "fe2630b38159ea7b9cf977b5fed40a9917002087"
SRCREV_meta_pn-linux-yocto-rt_fri2-noemgd ?= "5b4c9dc78b5ae607173cc3ddab9bce1b5f78129b"

module_autoload_iwlwifi = "iwlwifi"
