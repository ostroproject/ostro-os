FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_nuc = "nuc"
KMACHINE_nuc = "chiefriver"
KBRANCH_nuc = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_nuc = " features/amt/mei/mei.scc wifi"

LINUX_VERSION = "3.8.13"

SRCREV_meta_nuc = "acee86ed84e252f1c3af782cc3aa044aaa13e51a"
SRCREV_machine_nuc = "1f973c0fc8eea9a8f9758f47cf689ba89dbe9a25"

module_autoload_iwlwifi_nuc = "iwlwifi"
