FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_chiefriver = "chiefriver"
KMACHINE_chiefriver = "chiefriver"
KBRANCH_chiefriver = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_chiefriver = " features/amt/mei/mei.scc"

LINUX_VERSION = "3.10.19"

SRCREV_meta_chiefriver = "d9cd83c0292bd4e2a6754a96761027252e726a42"
SRCREV_machine_chiefriver = "a9ec82e355130160f9094e670bd5be0022a84194"
