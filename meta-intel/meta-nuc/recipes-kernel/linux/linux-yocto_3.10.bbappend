FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"


COMPATIBLE_MACHINE_nuc = "nuc"
KMACHINE_nuc = "chiefriver"
KBRANCH_nuc = "standard/base"

KERNEL_FEATURES_append_nuc = " features/amt/mei/mei.scc wifi"

LINUX_VERSION = "3.10.34"

SRCREV_meta_nuc = "df3aa753c8826127fb5ad811d56d57168551d6e4"
SRCREV_machine_nuc = "c7739be126930006e3bfbdb2fb070a967abc5e09"

module_autoload_iwlwifi_nuc = "iwlwifi"
