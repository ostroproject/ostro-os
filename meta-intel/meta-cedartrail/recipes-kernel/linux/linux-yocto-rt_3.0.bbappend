FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"
COMPATIBLE_MACHINE_cedartrail = "cedartrail"
KMACHINE_cedartrail  = "cedartrail"

KERNEL_FEATURES_append_cedartrail += " cfg/smp.scc"

# Update the following to use a different BSP branch or meta SRCREV
#KBRANCH_cedartrail  = "yocto/standard/preempt-rt/base"
#SRCREV_machine_pn-linux-yocto-rt_cedartrail ?= XXXX
#SRCREV_meta_pn-linux-yocto-rt_cedartrail ?= XXXX
