FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_nuc = "nuc"
KMACHINE_nuc = "chiefriver"
KBRANCH_nuc = "standard/base"

KERNEL_FEATURES_append_nuc = " features/amt/mei wifi"

LINUX_VERSION_nuc = "3.14.0"
SRCREV_machine_nuc = "0143c6ebb4a2d63b241df5f608b19f483f7eb9e0"
SRCREV_meta_nuc = "fc8c30398dbc3cdea787a1042242d4aab689d0ae"

module_autoload_iwlwifi_nuc = "iwlwifi"
