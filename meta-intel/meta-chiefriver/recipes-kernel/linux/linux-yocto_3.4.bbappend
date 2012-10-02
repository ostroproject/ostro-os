FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_chiefriver = "chiefriver"
KMACHINE_chiefriver  = "chiefriver"
KBRANCH_chiefriver  = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_chiefriver = " features/amt/mei"

SRCREV_machine_pn-linux-yocto_chiefriver ?= "3fa06aa29078fdb2af431de2d3fdae7d281ba85f"
SRCREV_meta_pn-linux-yocto_chiefriver ?= "5bdc655034a58a7147176a8a882d81e2fd51e4b9"
