FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"


COMPATIBLE_MACHINE_sys940x = "sys940x"
KMACHINE_sys940x  = "sys940x"
#KBRANCH_sys940x = "standard/default/base"
SRCREV_machine_pn-linux-yocto_sys940x ?= "f4f8ba730e7783e09413872414d0a17c142c816d"
SRCREV_meta_pn-linux-yocto_sys940x ?= "6b3d4e09aa2531e9649f3f03827b7efbccfcec03"

COMPATIBLE_MACHINE_sys940x-noemgd = "sys940x-noemgd"
KMACHINE_sys940x-noemgd  = "sys940x"
#KBRANCH_sys940x-noemgd = "standard/default/base"
SRCREV_machine_pn-linux-yocto_sys940x-noemgd ?= "f4f8ba730e7783e09413872414d0a17c142c816d"
SRCREV_meta_pn-linux-yocto_sys940x-noemgd ?= "6b3d4e09aa2531e9649f3f03827b7efbccfcec03"
