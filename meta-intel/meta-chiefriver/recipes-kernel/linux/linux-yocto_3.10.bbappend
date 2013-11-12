FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_chiefriver = "chiefriver"
KMACHINE_chiefriver = "chiefriver"
KBRANCH_chiefriver = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_chiefriver = " features/amt/mei/mei.scc"

LINUX_VERSION = "3.10.17"

SRCREV_meta_chiefriver = "f1c9080cd27f99700fa59b5375d1ddd0afe625ad"
SRCREV_machine_chiefriver = "c03195ed6e3066494e3fb4be69154a57066e845b"
