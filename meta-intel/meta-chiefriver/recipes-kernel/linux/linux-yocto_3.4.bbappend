FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_chiefriver = "chiefriver"
KMACHINE_chiefriver  = "chiefriver"
KBRANCH_chiefriver  = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_chiefriver = " features/amt/mei"

SRCREV_machine_pn-linux-yocto_chiefriver ?= "218bd8d2022b9852c60d32f0d770931e3cf343e2"
SRCREV_meta_pn-linux-yocto_chiefriver ?= "68a635bf8dfb64b02263c1ac80c948647cc76d5f"

LINUX_VERSION = "3.4.11"
