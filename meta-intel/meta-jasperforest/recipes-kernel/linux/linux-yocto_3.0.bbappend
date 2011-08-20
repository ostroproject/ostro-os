FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_jasperforest = "jasperforest"

KMACHINE_jasperforest  = "yocto/standard/common-pc-64/jasperforest"

SRCREV_machine_pn-linux-yocto_jasperforest ?= "bc7f933525ebc267cc8d9a66ce03626bbe14537b"
SRCREV_meta_pn-linux-yocto_jasperforest ?= "d588bdafc0d9b4d2386144b7d76a1d379e2d16c0"
