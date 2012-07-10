FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2 = "fri2"
#KBRANCH_fri2 = "standard/preempt-rt/fri2"
SRCREV_machine_pn-linux-yocto-rt_fri2 ?= "99554fd7da2605828ceda01a113bf826ec5a8229"
SRCREV_meta_pn-linux-yocto-rt_fri2 ?= "07ee09b520579b9f29bd15fefb01fd28b34c6064"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
#KBRANCH_fri2-noemgd = "standard/preempt-rt/fri2"
SRCREV_machine_pn-linux-yocto-rt_fri2-noemgd ?= "99554fd7da2605828ceda01a113bf826ec5a8229"
SRCREV_meta_pn-linux-yocto-rt_fri2-noemgd ?= "07ee09b520579b9f29bd15fefb01fd28b34c6064"

module_autoload_iwlwifi = "iwlwifi"
