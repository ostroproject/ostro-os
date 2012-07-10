FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"


COMPATIBLE_MACHINE_sys940x = "sys940x"
KMACHINE_sys940x  = "sys940x"
#KBRANCH_sys940x = "standard/default/base"
SRCREV_machine_pn-linux-yocto_sys940x ?= "7cc31a952f78b8f8e8469eed93c23e9675a8eeb5"
SRCREV_meta_pn-linux-yocto_sys940x ?= "07ee09b520579b9f29bd15fefb01fd28b34c6064"

COMPATIBLE_MACHINE_sys940x-noemgd = "sys940x-noemgd"
KMACHINE_sys940x-noemgd  = "sys940x"
#KBRANCH_sys940x-noemgd = "standard/default/base"
SRCREV_machine_pn-linux-yocto_sys940x-noemgd ?= "7cc31a952f78b8f8e8469eed93c23e9675a8eeb5"
SRCREV_meta_pn-linux-yocto_sys940x-noemgd ?= "07ee09b520579b9f29bd15fefb01fd28b34c6064"
