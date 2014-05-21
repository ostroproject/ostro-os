FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow-noemgd = "emenlow-noemgd"
KMACHINE_emenlow-noemgd  = "emenlow"

# Update the following to use a different BSP branch or meta SRCREV
#KBRANCH_emenlow-noemgd  = "standard/preempt-rt/base"
#SRCREV_machine_pn-linux-yocto-rt_emenlow-noemgd ?= XXXX
#SRCREV_meta_pn-linux-yocto-rt_emenlow-noemgd ?= XXXX
