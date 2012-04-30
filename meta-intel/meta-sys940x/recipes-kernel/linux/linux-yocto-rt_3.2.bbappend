FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_sys940x = "sys940x"
KMACHINE_sys940x = "sys940x"

COMPATIBLE_MACHINE_sys940x-noemgd = "sys940x-noemgd"
KMACHINE_sys940x-noemgd = "sys940x"

# Update the following to use a different BSP branch or meta SRCREV
#KBRANCH_sys940x = "standard/preempt-rt/base"
SRCREV_machine_pn-linux-yocto-rt_sys940x ?= "3ebf4d172cf4a41d2abf09e4036f0850e08064e7"
SRCREV_meta_pn-linux-yocto-rt_sys940x ?= "6b3d4e09aa2531e9649f3f03827b7efbccfcec03"
