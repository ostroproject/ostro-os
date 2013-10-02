FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_chiefriver = "chiefriver"
KMACHINE_chiefriver = "chiefriver"
KBRANCH_chiefriver = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_chiefriver = " features/amt/mei/mei.scc"

LINUX_VERSION = "3.10.11"

SRCREV_meta_chiefriver = "363bd856c8101d4227d492cc911bc4ca0c4987c6"
SRCREV_machine_chiefriver = "e1aa804148370cda6f85640281af156ffa007d52"
