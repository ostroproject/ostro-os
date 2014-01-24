FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

PACKAGE_ARCH_nuc = "${MACHINE_ARCH}"

COMPATIBLE_MACHINE_nuc = "nuc"
KMACHINE_nuc  = "chiefriver"
KBRANCH_nuc  = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_nuc = " features/amt/mei wifi"

SRCREV_machine_pn-linux-yocto_nuc ?= "de0c0ed674dfdbd808657e299fc720d8a97cb868"
SRCREV_meta_pn-linux-yocto_nuc ?= "9473a39c59bf9c07a316486d272652bacb9ad3ac"

module_autoload_iwlwifi_nuc = "iwlwifi"

LINUX_VERSION = "3.4.46"
