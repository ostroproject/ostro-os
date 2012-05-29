FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_chiefriver = "chiefriver"
KMACHINE_chiefriver  = "chiefriver"
KBRANCH_chiefriver  = "standard/default/common-pc-64/chiefriver"

KERNEL_FEATURES_append_chiefriver = " features/amt/mei"

SRCREV_machine_pn-linux-yocto_chiefriver ?= "b95a0ae3773545fa0ed9a47088d0361527c42e6c"
SRCREV_meta_pn-linux-yocto_chiefriver ?= "5b4c9dc78b5ae607173cc3ddab9bce1b5f78129b"
