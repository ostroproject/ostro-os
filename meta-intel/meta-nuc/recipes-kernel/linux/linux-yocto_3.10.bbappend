FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_nuc = "nuc"
KMACHINE_nuc = "chiefriver"
KBRANCH_nuc = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_nuc = " features/amt/mei/mei.scc wifi"

LINUX_VERSION = "3.10.17"

SRCREV_meta_nuc = "f1c9080cd27f99700fa59b5375d1ddd0afe625ad"
SRCREV_machine_nuc = "c03195ed6e3066494e3fb4be69154a57066e845b"

module_autoload_iwlwifi_nuc = "iwlwifi"
