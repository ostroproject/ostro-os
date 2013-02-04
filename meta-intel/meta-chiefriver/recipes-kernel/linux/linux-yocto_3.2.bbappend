FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_chiefriver = "chiefriver"
KMACHINE_chiefriver  = "chiefriver"
KBRANCH_chiefriver  = "standard/default/common-pc-64/chiefriver"

KERNEL_FEATURES_append_chiefriver = " features/amt/mei"

SRCREV_machine_pn-linux-yocto_chiefriver ?= "825530551f81def14485936340e088f77941f0b1"
SRCREV_meta_pn-linux-yocto_chiefriver ?= "e7f2fdc48f8808887175f0328274a2668084738c"

LINUX_VERSION = "3.2.32"
