FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_chiefriver = "chiefriver"
KMACHINE_chiefriver  = "chiefriver"
KBRANCH_chiefriver  = "standard/common-pc-64/chiefriver"

KERNEL_FEATURES_append_chiefriver = " features/amt/mei"

SRCREV_machine_pn-linux-yocto_chiefriver ?= "6297e4c1d57e1063bfce297c2e12392348598559"
SRCREV_meta_pn-linux-yocto_chiefriver ?= "c2b5ee363bf2612932301488f3ac0644ff70fc7c"
