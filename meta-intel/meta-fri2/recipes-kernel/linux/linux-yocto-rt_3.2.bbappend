FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2 = "fri2"
#KBRANCH_fri2 = "standard/preempt-rt/fri2"
SRCREV_machine_pn-linux-yocto-rt_fri2 ?= "83e81b247fbaa40330c3a694f3725c7fb2b8ec2e"
SRCREV_meta_pn-linux-yocto-rt_fri2 ?= "ee78519365bdb25287703bbc31c06b193263c654"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
#KBRANCH_fri2-noemgd = "standard/preempt-rt/fri2"
SRCREV_machine_pn-linux-yocto-rt_fri2-noemgd ?= "83e81b247fbaa40330c3a694f3725c7fb2b8ec2e"
SRCREV_meta_pn-linux-yocto-rt_fri2-noemgd ?= "ee78519365bdb25287703bbc31c06b193263c654"

module_autoload_iwlwifi = "iwlwifi"
