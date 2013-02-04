FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"


COMPATIBLE_MACHINE_sys940x = "sys940x"
KMACHINE_sys940x  = "sys940x"
#KBRANCH_sys940x = "standard/default/base"
SRCREV_machine_pn-linux-yocto_sys940x ?= "6970a8f4f7caa2633aa1ae0b51732b246eb581ef"
SRCREV_meta_pn-linux-yocto_sys940x ?= "e7f2fdc48f8808887175f0328274a2668084738c"

COMPATIBLE_MACHINE_sys940x-noemgd = "sys940x-noemgd"
KMACHINE_sys940x-noemgd  = "sys940x"
#KBRANCH_sys940x-noemgd = "standard/default/base"
SRCREV_machine_pn-linux-yocto_sys940x-noemgd ?= "6970a8f4f7caa2633aa1ae0b51732b246eb581ef"
SRCREV_meta_pn-linux-yocto_sys940x-noemgd ?= "e7f2fdc48f8808887175f0328274a2668084738c"

LINUX_VERSION = "3.2.32"
