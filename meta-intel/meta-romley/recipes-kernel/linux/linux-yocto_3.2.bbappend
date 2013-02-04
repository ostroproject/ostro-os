FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_romley = "romley"

KMACHINE_romley  = "romley"
KBRANCH_romley  = "standard/default/common-pc-64/romley"

SRCREV_machine_pn-linux-yocto_romley ?= "f80ca865245b0a269e732d42f1e6f64849505662"
SRCREV_meta_pn-linux-yocto_romley ?= "e7f2fdc48f8808887175f0328274a2668084738c"

LINUX_VERSION = "3.2.32"
