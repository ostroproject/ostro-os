FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_chiefriver = "chiefriver"
KMACHINE_chiefriver  = "chiefriver"
KBRANCH_chiefriver  = "standard/default/common-pc-64/chiefriver"

KERNEL_FEATURES_append_chiefriver = " features/amt/mei"

SRCREV_machine_pn-linux-yocto_chiefriver ?= "edfd9a30a020fa1e6d2273edaceca19594b487f0"
SRCREV_meta_pn-linux-yocto_chiefriver ?= "07ee09b520579b9f29bd15fefb01fd28b34c6064"
