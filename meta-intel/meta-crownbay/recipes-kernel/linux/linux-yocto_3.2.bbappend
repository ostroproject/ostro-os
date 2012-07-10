FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay  = "crownbay"
KBRANCH_crownbay  = "standard/default/crownbay"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd  = "crownbay"
KBRANCH_crownbay-noemgd  = "standard/default/crownbay"

SRCREV_machine_pn-linux-yocto_crownbay ?= "ddcccbf870485c835f9b4b94823ca0c4186d78df"
SRCREV_meta_pn-linux-yocto_crownbay ?= "07ee09b520579b9f29bd15fefb01fd28b34c6064"

SRCREV_machine_pn-linux-yocto_crownbay-noemgd ?= "ddcccbf870485c835f9b4b94823ca0c4186d78df"
SRCREV_meta_pn-linux-yocto_crownbay-noemgd ?= "07ee09b520579b9f29bd15fefb01fd28b34c6064"
