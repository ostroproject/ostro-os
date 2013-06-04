FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_chiefriver = "chiefriver"
KMACHINE_chiefriver = "chiefriver"
KBRANCH_chiefriver = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_chiefriver = " features/amt/mei/mei.scc"

LINUX_VERSION = "3.8.11"

SRCREV_machine_chiefriver = "6ed6ca790b7afef5881de4566850bbc30ae26df6"
SRCREV_meta_chiefriver = "edd6461602f6c2fc27bc72997e4437f422a9dccd"
