FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"


COMPATIBLE_MACHINE_sys940x = "sys940x"
KMACHINE_sys940x  = "sys940x"
KBRANCH_sys940x = "yocto/standard/base"
KERNEL_FEATURES_append_sys940x += " cfg/smp.scc cfg/efi-ext.scc"

COMPATIBLE_MACHINE_sys940x-noemgd = "sys940x-noemgd"
KMACHINE_sys940x-noemgd  = "sys940x"
KBRANCH_sys940x-noemgd = "yocto/standard/base"
KERNEL_FEATURES_append_sys940x-noemgd += " cfg/smp.scc cfg/efi-ext.scc"

SRCREV_machine_pn-linux-yocto_sys940x ?= "5df0b4c2538399aed543133b3855f809adf08ab8"
SRCREV_meta_pn-linux-yocto_sys940x ?= "77ca4855e80acb8dad21acea946908716c308b5b"
SRCREV_machine_pn-linux-yocto_sys940x-noemgd ?= "5df0b4c2538399aed543133b3855f809adf08ab8"
SRCREV_meta_pn-linux-yocto_sys940x-noemgd ?= "77ca4855e80acb8dad21acea946908716c308b5b"
