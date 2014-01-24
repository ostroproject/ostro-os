FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

PACKAGE_ARCH_crownbay = "${MACHINE_ARCH}"
PACKAGE_ARCH_crownbay-noemgd = "${MACHINE_ARCH}"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd = "crownbay"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay = "crownbay"

# Update the following to use a different BSP branch or meta SRCREV
#KBRANCH_crownbay-noemgd = "standard/preempt-rt/base"
#SRCREV_machine_pn-linux-yocto-rt_crownbay-noemgd ?= XXXX
#SRCREV_meta_pn-linux-yocto-rt_crownbay-noemgd ?= XXXX

#KBRANCH_crownbay = "standard/preempt-rt/base"
#SRCREV_machine_pn-linux-yocto-rt_crownbay ?= XXXX
#SRCREV_meta_pn-linux-yocto-rt_crownbay ?= XXXX
