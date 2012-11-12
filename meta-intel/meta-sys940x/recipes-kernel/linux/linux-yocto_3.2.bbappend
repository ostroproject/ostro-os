FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"


COMPATIBLE_MACHINE_sys940x = "sys940x"
KMACHINE_sys940x  = "sys940x"
#KBRANCH_sys940x = "standard/default/base"
SRCREV_machine_pn-linux-yocto_sys940x ?= "${AUTOREV}"
SRCREV_meta_pn-linux-yocto_sys940x ?= "${AUTOREV}"

COMPATIBLE_MACHINE_sys940x-noemgd = "sys940x-noemgd"
KMACHINE_sys940x-noemgd  = "sys940x"
#KBRANCH_sys940x-noemgd = "standard/default/base"
SRCREV_machine_pn-linux-yocto_sys940x-noemgd ?= "${AUTOREV}"
SRCREV_meta_pn-linux-yocto_sys940x-noemgd ?= "${AUTOREV}"
