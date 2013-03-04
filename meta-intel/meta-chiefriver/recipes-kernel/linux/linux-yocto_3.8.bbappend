FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_chiefriver = "chiefriver"
KMACHINE_chiefriver = "chiefriver"
KBRANCH_chiefriver = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_chiefriver = " features/amt/mei"

SRCREV_machine_chiefriver = "b170394a475b96ecc92cbc9e4b002bed0a9f69c5"
SRCREV_meta_chiefriver = "c2ed0f16fdec628242a682897d5d86df4547cf24"
