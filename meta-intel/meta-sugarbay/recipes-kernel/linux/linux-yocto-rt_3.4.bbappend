FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"
PACKAGE_ARCH_sugarbay = "${MACHINE_ARCH}"
COMPATIBLE_MACHINE_sugarbay = "sugarbay"
KMACHINE_sugarbay  = "sugarbay"

# Update the following to use a different BSP branch or meta SRCREV
#KBRANCH_sugarbay  = "standard/preempt-rt/base"
#SRCREV_machine_pn-linux-yocto-rt_sugarbay ?= XXXX
#SRCREV_meta_pn-linux-yocto-rt_sugarbay ?= XXXX
