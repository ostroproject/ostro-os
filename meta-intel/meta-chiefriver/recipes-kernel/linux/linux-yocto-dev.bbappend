FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"


COMPATIBLE_MACHINE_chiefriver = "chiefriver"
KMACHINE_chiefriver = "chiefriver"
KBRANCH_chiefriver = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_chiefriver = " features/amt/mei"

SRCREV_machine_chiefriver = "60536206ad300ccf5b2be2c2d449f4ab27170238"
SRCREV_meta_chiefriver = "fe20c99783387dab779472ff50a88666da1c6391"
