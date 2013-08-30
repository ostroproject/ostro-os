FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_nuc = "nuc"
KMACHINE_nuc = "chiefriver"
KBRANCH_nuc = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_nuc = " features/amt/mei/mei.scc wifi"

LINUX_VERSION = "3.10.10"

SRCREV_meta_nuc = "ea900d1db60ba48962227f0976ac55f9e25bfa24"
SRCREV_machine_nuc = "ebc8428fdd938cfdfcdcadd77c3308ece6a57de1"

module_autoload_iwlwifi_nuc = "iwlwifi"
