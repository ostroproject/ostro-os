FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2  = "fri2"
KBRANCH_fri2 = "standard/default/fri2"
SRCREV_machine_pn-linux-yocto_fri2 ?= "5f802fa5b7452454ae221ca8a527918a30f6a914"
SRCREV_meta_pn-linux-yocto_fri2 ?= "e7f2fdc48f8808887175f0328274a2668084738c"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd  = "fri2"
KBRANCH_fri2-noemgd = "standard/default/fri2"
SRCREV_machine_pn-linux-yocto_fri2-noemgd ?= "5f802fa5b7452454ae221ca8a527918a30f6a914"
SRCREV_meta_pn-linux-yocto_fri2-noemgd ?= "e7f2fdc48f8808887175f0328274a2668084738c"

module_autoload_iwlwifi = "iwlwifi"

LINUX_VERSION = "3.2.32"
