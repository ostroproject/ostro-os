FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"
PACKAGE_ARCH_chiefriver = "${MACHINE_ARCH}"
COMPATIBLE_MACHINE_chiefriver = "chiefriver"
KMACHINE_chiefriver  = "chiefriver"

# Update the following to use a different BSP branch or meta SRCREV
#KBRANCH_chiefriver  = "standard/preempt-rt/base"
#SRCREV_machine_pn-linux-yocto-rt_chiefriver ?= XXXX
#SRCREV_meta_pn-linux-yocto-rt_chiefriver ?= XXXX
