FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_chiefriver = "chiefriver"
KMACHINE_chiefriver = "chiefriver"
KBRANCH_chiefriver = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_chiefriver = " features/amt/mei/mei.scc"

LINUX_VERSION = "3.8.13"

SRCREV_machine_chiefriver = "1f973c0fc8eea9a8f9758f47cf689ba89dbe9a25"
SRCREV_meta_chiefriver = "acee86ed84e252f1c3af782cc3aa044aaa13e51a"
