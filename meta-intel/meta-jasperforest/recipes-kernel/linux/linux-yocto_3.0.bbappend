FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_jasperforest = "jasperforest"

KMACHINE_jasperforest  = "yocto/standard/common-pc-64/jasperforest"

SRCREV_machine_pn-linux-yocto_jasperforest ?= "4a133efaefd3f841254e1b3ba65c91923d7548a5"
SRCREV_meta_pn-linux-yocto_jasperforest ?= "67a46a608f47c19f16995be7de7b272025864b1b"
