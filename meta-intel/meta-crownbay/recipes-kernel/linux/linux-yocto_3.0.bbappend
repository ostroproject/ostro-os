FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay  = "yocto/standard/crownbay"
KERNEL_FEATURES_append_crownbay += " cfg/smp.scc"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd  = "yocto/standard/crownbay"
KERNEL_FEATURES_append_crownbay-noemgd += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto_crownbay ?= "8800e8c8107e70ef84fd8b9b0ac0c7f7402b2d89"
SRCREV_meta_pn-linux-yocto_crownbay ?= "67ce7623909cef63927fd145026aaf371cf4abf1"

SRCREV_machine_pn-linux-yocto_crownbay-noemgd ?= "8800e8c8107e70ef84fd8b9b0ac0c7f7402b2d89"
SRCREV_meta_pn-linux-yocto_crownbay-noemgd ?= "67ce7623909cef63927fd145026aaf371cf4abf1"
