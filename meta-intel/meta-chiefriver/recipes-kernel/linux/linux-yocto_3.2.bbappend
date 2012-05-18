FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_chiefriver = "chiefriver"
KMACHINE_chiefriver  = "chiefriver"
KBRANCH_chiefriver  = "standard/default/common-pc-64/chiefriver"

SRCREV_machine_pn-linux-yocto_chiefriver ?= "dbe820c277dfa6cbc249d410e8b083286ec484b7"
SRCREV_meta_pn-linux-yocto_chiefriver ?= "353d43d340e87996b4be4c5f6ddb4447e050b65c"
