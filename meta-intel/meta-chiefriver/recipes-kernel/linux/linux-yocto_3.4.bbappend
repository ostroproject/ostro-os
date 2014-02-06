FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"


COMPATIBLE_MACHINE_chiefriver = "chiefriver"
KMACHINE_chiefriver  = "chiefriver"
KBRANCH_chiefriver  = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_chiefriver = " features/amt/mei"

SRCREV_machine_pn-linux-yocto_chiefriver ?= "de0c0ed674dfdbd808657e299fc720d8a97cb868"
SRCREV_meta_pn-linux-yocto_chiefriver ?= "9473a39c59bf9c07a316486d272652bacb9ad3ac"

LINUX_VERSION = "3.4.46"
