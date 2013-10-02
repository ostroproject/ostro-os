FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_chiefriver = "chiefriver"
KMACHINE_chiefriver = "chiefriver"
KBRANCH_chiefriver = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_chiefriver = " features/amt/mei/mei.scc"

LINUX_VERSION = "3.8.13"

SRCREV_meta_chiefriver = "467a74c47bd70c52d0b81597007d8cc39cadaefd"
SRCREV_machine_chiefriver = "f20047520a57322f05d95a18a5fbd082fb15cb87"
