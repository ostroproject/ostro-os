FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_sys940x = "sys940x"
KMACHINE_sys940x = "sys940x"

COMPATIBLE_MACHINE_sys940x-noemgd = "sys940x-noemgd"
KMACHINE_sys940x-noemgd = "sys940x"

# Update the following to use a different BSP branch or meta SRCREV
#KBRANCH_sys940x = "standard/preempt-rt/base"
SRCREV_machine_pn-linux-yocto-rt_sys940x ?= "d8f7347b67d909a999391c4b6f64447b0ccdc86a"
SRCREV_meta_pn-linux-yocto-rt_sys940x ?= "e7f2fdc48f8808887175f0328274a2668084738c"

LINUX_VERSION = "3.2.32"
