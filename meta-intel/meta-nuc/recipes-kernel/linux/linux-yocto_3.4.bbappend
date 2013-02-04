FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_nuc = "nuc"
KMACHINE_nuc  = "chiefriver"
KBRANCH_nuc  = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_nuc = " features/amt/mei wifi"

SRCREV_machine_pn-linux-yocto_nuc ?= "13809f2cfd9be0ce86bd486e1643f9b90bed6f4f"
SRCREV_meta_pn-linux-yocto_nuc ?= "f697e099bc76d5df3a307a5bc0cc25021dd6dfe0"

module_autoload_iwlwifi_nuc = "iwlwifi"

LINUX_VERSION = "3.4.28"
