FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_nuc = "nuc"
KMACHINE_nuc = "chiefriver"
KBRANCH_nuc = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_nuc = " features/amt/mei/mei.scc wifi"

LINUX_VERSION = "3.10.11"

SRCREV_meta_nuc = "452f0679ea93a6cb4433bebd7177629228a5cf68"
SRCREV_machine_nuc = "2927821e14523fa0ee18140aa7ff6e0509b48ab7"

module_autoload_iwlwifi_nuc = "iwlwifi"
