FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_nuc = "nuc"
KMACHINE_nuc = "chiefriver"
KBRANCH_nuc = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_nuc = " features/amt/mei wifi"

SRCREV_meta_nuc = "c2ed0f16fdec628242a682897d5d86df4547cf24"
SRCREV_machine_nuc = "b170394a475b96ecc92cbc9e4b002bed0a9f69c5"

module_autoload_iwlwifi_nuc = "iwlwifi"
