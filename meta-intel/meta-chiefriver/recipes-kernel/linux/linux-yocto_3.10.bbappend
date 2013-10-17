FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_chiefriver = "chiefriver"
KMACHINE_chiefriver = "chiefriver"
KBRANCH_chiefriver = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_chiefriver = " features/amt/mei/mei.scc"

LINUX_VERSION = "3.10.11"

SRCREV_meta_chiefriver = "452f0679ea93a6cb4433bebd7177629228a5cf68"
SRCREV_machine_chiefriver = "2927821e14523fa0ee18140aa7ff6e0509b48ab7"
