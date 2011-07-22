FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"
COMPATIBLE_MACHINE_sugarbay = "sugarbay"
KMACHINE_sugarbay  = "sugarbay"
KBRANCH_sugarbay  = "yocto/standard/preempt-rt/base"

SRCREV_machine_pn-linux-yocto-rt_sugarbay ?= ${AUTOREV}
SRCREV_meta_pn-linux-yocto-rt_sugarbay ?= ${AUTOREV}
