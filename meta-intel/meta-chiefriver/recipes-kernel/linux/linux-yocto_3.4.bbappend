FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_chiefriver = "chiefriver"
KMACHINE_chiefriver  = "chiefriver"
KBRANCH_chiefriver  = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_chiefriver = " features/amt/mei"

SRCREV_machine_pn-linux-yocto_chiefriver ?= "449f7f520350700858f21a5554b81cc8ad23267d"
SRCREV_meta_pn-linux-yocto_chiefriver ?= "9e3bdb7344054264b750e53fbbb6394cc1c942ac"
