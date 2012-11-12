FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_romley = "romley"

KMACHINE_romley  = "romley"
KBRANCH_romley  = "standard/default/common-pc-64/romley"

SRCREV_machine_pn-linux-yocto_romley ?= "${AUTOREV}"
SRCREV_meta_pn-linux-yocto_romley ?= "${AUTOREV}"
