FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"


COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd = "crownbay"

# Update the following to use a different BSP branch or meta SRCREV
#KBRANCH_crownbay-noemgd = "standard/preempt-rt/base"
#SRCREV_machine_pn-linux-yocto-rt_crownbay-noemgd ?= XXXX
#SRCREV_meta_pn-linux-yocto-rt_crownbay-noemgd ?= XXXX
