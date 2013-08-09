FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_nuc = "nuc"
KMACHINE_nuc = "chiefriver"
KBRANCH_nuc = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_nuc = " features/amt/mei/mei.scc wifi"

LINUX_VERSION = "3.8.13"

SRCREV_meta_nuc = "f706bd410c80a20ff437a53bb3f9f076ba31a17e"
SRCREV_machine_nuc = "f20047520a57322f05d95a18a5fbd082fb15cb87"

module_autoload_iwlwifi_nuc = "iwlwifi"
