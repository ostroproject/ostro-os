FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_nuc = "nuc"
KMACHINE_nuc = "chiefriver"
KBRANCH_nuc = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_nuc = " features/amt/mei wifi"

LINUX_VERSION = "3.8.4"

SRCREV_meta_nuc = "2a6d36e75ca0a121570a389d7bab76ec240cbfda"
SRCREV_machine_nuc = "47aed0c17c1c55988198ad39f86ae88894c8e0a4"

module_autoload_iwlwifi_nuc = "iwlwifi"
