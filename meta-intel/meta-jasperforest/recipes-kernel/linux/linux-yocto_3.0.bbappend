FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_jasperforest = "jasperforest"

KMACHINE_jasperforest  = "yocto/standard/common-pc-64/jasperforest"

SRCREV_machine_pn-linux-yocto_jasperforest ?= "56ed5e7b8af6e908b8c6abf75498ab64c87e192d"
SRCREV_meta_pn-linux-yocto_jasperforest ?= "82140b960a7cc13d116be61a85d4fe7f7d38680f"
