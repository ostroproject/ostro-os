FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2  = "fri2"
KBRANCH_fri2 = "standard/fri2"
SRCREV_machine_pn-linux-yocto_fri2 ?= "59c3ff750831338d05ab67d5efd7fc101c451aff"
#SRCREV_meta_pn-linux-yocto_fri2 ?= "c5bddf8ea379406ffec550528e17b777a0eba24b"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd  = "fri2"
KBRANCH_fri2-noemgd = "standard/fri2"
SRCREV_machine_pn-linux-yocto_fri2-noemgd ?= "59c3ff750831338d05ab67d5efd7fc101c451aff"
#SRCREV_meta_pn-linux-yocto_fri2-noemgd ?= "c5bddf8ea379406ffec550528e17b777a0eba24b"

module_autoload_iwlwifi = "iwlwifi"
