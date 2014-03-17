FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_sys940x = "sys940x"
KMACHINE_sys940x = "sys940x"

COMPATIBLE_MACHINE_sys940x-noemgd = "sys940x-noemgd"
KMACHINE_sys940x-noemgd = "sys940x"

# Update the following to use a different BSP branch or meta SRCREV
#KBRANCH_sys940x = "standard/preempt-rt/base"
#SRCREV_machine_pn-linux-yocto-rt_sys940x ?= "XXX"
#SRCREV_meta_pn-linux-yocto-rt_sys940x ?= "XXX"

#KBRANCH_sys940x-noemgd = "standard/preempt-rt/base"
#SRCREV_machine_pn-linux-yocto-rt_sys940x-noemgd ?= "XXX"
#SRCREV_meta_pn-linux-yocto-rt_sys940x-noemgd ?= "XXX"
