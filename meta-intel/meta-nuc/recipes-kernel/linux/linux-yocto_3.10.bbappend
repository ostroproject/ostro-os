FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_nuc = "nuc"
KMACHINE_nuc = "chiefriver"
KBRANCH_nuc = "standard/base"

KERNEL_FEATURES_append_nuc = " features/amt/mei/mei.scc wifi"

LINUX_VERSION_nuc = "3.10.35"
SRCREV_meta_nuc = "b6e58b33dd427fe471f8827c83e311acdf4558a4"
SRCREV_machine_nuc = "cee957655fe67826b2e827e2db41f156fa8f0cc4"

module_autoload_iwlwifi_nuc = "iwlwifi"
