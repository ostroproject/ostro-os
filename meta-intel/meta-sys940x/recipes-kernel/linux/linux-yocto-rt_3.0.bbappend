FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_sys940x = "sys940x"
KMACHINE_sys940x = "sys940x"
KERNEL_FEATURES_append_sys940x += " cfg/smp.scc cfg/efi-ext.scc"

COMPATIBLE_MACHINE_sys940x-noemgd = "sys940x-noemgd"
KMACHINE_sys940x-noemgd = "sys940x"
KERNEL_FEATURES_append_sys940x-noemgd += " cfg/smp.scc cfg/efi-ext.scc"

# Update the following to use a different BSP branch or meta SRCREV
#KBRANCH_sys940x = "yocto/standard/preempt-rt/base"
#SRCREV_machine_pn-linux-yocto-rt_sys940x ?= XXXX
#SRCREV_meta_pn-linux-yocto-rt_sys940x ?= XXXX
