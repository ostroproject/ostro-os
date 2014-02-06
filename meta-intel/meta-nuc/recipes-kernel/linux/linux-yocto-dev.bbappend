FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"


COMPATIBLE_MACHINE_nuc = "nuc"
KMACHINE_nuc = "chiefriver"
KBRANCH_nuc = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_nuc = " features/amt/mei wifi"

SRCREV_machine_nuc = "60536206ad300ccf5b2be2c2d449f4ab27170238"
SRCREV_meta_nuc = "fe20c99783387dab779472ff50a88666da1c6391"

module_autoload_iwlwifi_nuc = "iwlwifi"
