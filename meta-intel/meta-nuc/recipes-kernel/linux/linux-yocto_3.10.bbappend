FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_nuc = "nuc"
KMACHINE_nuc = "chiefriver"
KBRANCH_nuc = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_nuc = " features/amt/mei/mei.scc wifi"

LINUX_VERSION = "3.10.19"

SRCREV_meta_nuc = "d9cd83c0292bd4e2a6754a96761027252e726a42"
SRCREV_machine_nuc = "a9ec82e355130160f9094e670bd5be0022a84194"

module_autoload_iwlwifi_nuc = "iwlwifi"
