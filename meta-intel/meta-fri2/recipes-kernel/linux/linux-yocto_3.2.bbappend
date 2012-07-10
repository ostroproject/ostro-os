FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2  = "fri2"
KBRANCH_fri2 = "standard/default/fri2"
SRCREV_machine_pn-linux-yocto_fri2 ?= "046bef8ea4dbb9c279e49ad9faf240b86fc80fdc"
SRCREV_meta_pn-linux-yocto_fri2 ?= "07ee09b520579b9f29bd15fefb01fd28b34c6064"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd  = "fri2"
KBRANCH_fri2-noemgd = "standard/default/fri2"
SRCREV_machine_pn-linux-yocto_fri2-noemgd ?= "046bef8ea4dbb9c279e49ad9faf240b86fc80fdc"
SRCREV_meta_pn-linux-yocto_fri2-noemgd ?= "07ee09b520579b9f29bd15fefb01fd28b34c6064"

module_autoload_iwlwifi = "iwlwifi"
