FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_chiefriver = "chiefriver"
KMACHINE_chiefriver  = "chiefriver"
KBRANCH_chiefriver  = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_chiefriver = " features/amt/mei"

SRCREV_machine_pn-linux-yocto_chiefriver ?= "59c3ff750831338d05ab67d5efd7fc101c451aff"
SRCREV_meta_pn-linux-yocto_chiefriver ?= "594994cb4c19bb4f2e8100ffe0599aef8b2e8b4c"
