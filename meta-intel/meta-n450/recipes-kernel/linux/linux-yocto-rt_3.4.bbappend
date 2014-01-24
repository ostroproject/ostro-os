FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"
PACKAGE_ARCH_n450 = "${MACHINE_ARCH}"
COMPATIBLE_MACHINE_n450 = "n450"
KMACHINE_n450 = "atom-pc"

# Update the following to use a different BSP branch or meta SRCREV
#KBRANCH_n450 = "yocto/standard/preempt-rt/base"
#SRCREV_machine_pn-linux-yocto-rt_n450 ?= XXXX
#SRCREV_meta_pn-linux-yocto-rt_n450 ?= XXXX
