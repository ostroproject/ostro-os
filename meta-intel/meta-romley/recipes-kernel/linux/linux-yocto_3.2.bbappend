FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_romley = "romley"

KMACHINE_romley  = "romley"
KBRANCH_romley  = "standard/default/common-pc-64/romley"

SRCREV_machine_pn-linux-yocto_romley ?= "5c7f1c53b5b367858ae6a86c1d4de36d8c71bedb"
SRCREV_meta_pn-linux-yocto_romley ?= "135c75bf9615334b5b8bb9108d612fe7dfbdb901"
