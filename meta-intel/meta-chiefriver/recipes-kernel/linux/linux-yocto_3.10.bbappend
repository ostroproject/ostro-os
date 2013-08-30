FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_chiefriver = "chiefriver"
KMACHINE_chiefriver = "chiefriver"
KBRANCH_chiefriver = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_chiefriver = " features/amt/mei/mei.scc"

LINUX_VERSION = "3.10.10"

SRCREV_meta_chiefriver = "ea900d1db60ba48962227f0976ac55f9e25bfa24"
SRCREV_machine_chiefriver = "ebc8428fdd938cfdfcdcadd77c3308ece6a57de1"
