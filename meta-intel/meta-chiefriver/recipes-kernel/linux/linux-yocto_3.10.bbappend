FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_chiefriver = "chiefriver"
KMACHINE_chiefriver = "chiefriver"
KBRANCH_chiefriver = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_chiefriver = " features/amt/mei/mei.scc"

LINUX_VERSION = "3.10.11"

SRCREV_meta_chiefriver = "285f93bf942e8f6fa678ffc6cc53696ed5400718"
SRCREV_machine_chiefriver = "702040ac7c7ec66a29b4d147665ccdd0ff015577"
