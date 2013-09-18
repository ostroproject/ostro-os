FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_nuc = "nuc"
KMACHINE_nuc = "chiefriver"
KBRANCH_nuc = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_nuc = " features/amt/mei/mei.scc wifi"

LINUX_VERSION = "3.10.11"

SRCREV_meta_nuc = "285f93bf942e8f6fa678ffc6cc53696ed5400718"
SRCREV_machine_nuc = "702040ac7c7ec66a29b4d147665ccdd0ff015577"

module_autoload_iwlwifi_nuc = "iwlwifi"
