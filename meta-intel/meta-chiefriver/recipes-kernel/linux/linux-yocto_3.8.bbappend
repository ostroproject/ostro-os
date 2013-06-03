FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_chiefriver = "chiefriver"
KMACHINE_chiefriver = "chiefriver"
KBRANCH_chiefriver = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_chiefriver = " features/amt/mei/mei.scc"

LINUX_VERSION = "3.8.4"

SRCREV_machine_chiefriver = "47aed0c17c1c55988198ad39f86ae88894c8e0a4"
SRCREV_meta_chiefriver = "2a6d36e75ca0a121570a389d7bab76ec240cbfda"
