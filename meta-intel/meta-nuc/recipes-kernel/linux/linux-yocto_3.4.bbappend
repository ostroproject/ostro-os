FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_nuc = "nuc"
KMACHINE_nuc  = "chiefriver"
KBRANCH_nuc  = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_nuc = " features/amt/mei wifi"

SRCREV_machine_pn-linux-yocto_nuc ?= "${AUTOREV}"
SRCREV_meta_pn-linux-yocto_nuc ?= "${AUTOREV}"

module_autoload_iwlwifi_nuc = "iwlwifi"
