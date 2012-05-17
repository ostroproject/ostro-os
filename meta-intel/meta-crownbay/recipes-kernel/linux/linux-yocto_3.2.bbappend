FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay  = "crownbay"
KBRANCH_crownbay  = "standard/default/crownbay"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd  = "crownbay"
KBRANCH_crownbay-noemgd  = "standard/default/crownbay"

SRCREV_machine_pn-linux-yocto_crownbay ?= "7a32032661d264b0bd63e5607fef79cf247f18a5"
SRCREV_meta_pn-linux-yocto_crownbay ?= "49f931bc294d5b6be60502bbd448cff5aa766235"

SRCREV_machine_pn-linux-yocto_crownbay-noemgd ?= "7a32032661d264b0bd63e5607fef79cf247f18a5"
SRCREV_meta_pn-linux-yocto_crownbay-noemgd ?= "49f931bc294d5b6be60502bbd448cff5aa766235"
