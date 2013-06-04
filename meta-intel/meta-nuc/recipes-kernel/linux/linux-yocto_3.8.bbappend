FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_nuc = "nuc"
KMACHINE_nuc = "chiefriver"
KBRANCH_nuc = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_nuc = " features/amt/mei/mei.scc wifi"

LINUX_VERSION = "3.8.11"

SRCREV_meta_nuc = "edd6461602f6c2fc27bc72997e4437f422a9dccd"
SRCREV_machine_nuc = "6ed6ca790b7afef5881de4566850bbc30ae26df6"

module_autoload_iwlwifi_nuc = "iwlwifi"
