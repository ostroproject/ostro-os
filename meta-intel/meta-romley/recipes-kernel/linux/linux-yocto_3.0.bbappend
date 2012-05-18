FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_romley = "romley"
KMACHINE_romley  = "romley"
KBRANCH_romley  = "yocto/standard/common-pc-64/romley"

SRCREV_machine_pn-linux-yocto_romley ?= "d26ab3559d75d0a3946ecaef67d3aeb7e9e7ef22"
SRCREV_meta_pn-linux-yocto_romley ?= "67ce7623909cef63927fd145026aaf371cf4abf1"
