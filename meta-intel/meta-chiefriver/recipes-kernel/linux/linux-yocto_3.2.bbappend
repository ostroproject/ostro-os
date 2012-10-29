FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_chiefriver = "chiefriver"
KMACHINE_chiefriver  = "chiefriver"
KBRANCH_chiefriver  = "standard/default/common-pc-64/chiefriver"

KERNEL_FEATURES_append_chiefriver = " features/amt/mei"

SRCREV_machine_pn-linux-yocto_chiefriver ?= "56d1c9ec36287350d154a3abef339598ef4028c2"
SRCREV_meta_pn-linux-yocto_chiefriver ?= "486f7aec824b4127e91ef53228823e996b3696f0"

LINUX_VERSION = "3.2.18"
