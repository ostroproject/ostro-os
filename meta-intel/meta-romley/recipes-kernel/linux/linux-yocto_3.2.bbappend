FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_romley = "romley"

KMACHINE_romley  = "romley"
KBRANCH_romley  = "standard/default/common-pc-64/romley"

SRCREV_machine_pn-linux-yocto_romley ?= "34e3cd8b7a1d18594a63b7b299fce46e32a6c80c"
SRCREV_meta_pn-linux-yocto_romley ?= "486f7aec824b4127e91ef53228823e996b3696f0"

LINUX_VERSION = "3.2.18"
