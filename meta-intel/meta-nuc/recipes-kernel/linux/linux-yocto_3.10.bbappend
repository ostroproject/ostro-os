FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_nuc = "nuc"
KMACHINE_nuc = "chiefriver"
KBRANCH_nuc = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_nuc = " features/amt/mei/mei.scc wifi"

LINUX_VERSION = "3.10.11"

SRCREV_meta_nuc = "363bd856c8101d4227d492cc911bc4ca0c4987c6"
SRCREV_machine_nuc = "e1aa804148370cda6f85640281af156ffa007d52"

module_autoload_iwlwifi_nuc = "iwlwifi"
