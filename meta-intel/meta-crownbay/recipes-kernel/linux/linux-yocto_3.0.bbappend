FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay  = "yocto/standard/crownbay"
KERNEL_FEATURES_append_crownbay += " cfg/smp.scc"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd  = "yocto/standard/crownbay"
KERNEL_FEATURES_append_crownbay-noemgd += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto_crownbay ?= "ef471cc8ba265072a02547f18a3b83dee5fa93a9"
SRCREV_meta_pn-linux-yocto_crownbay ?= "82140b960a7cc13d116be61a85d4fe7f7d38680f"

SRCREV_machine_pn-linux-yocto_crownbay-noemgd ?= "ef471cc8ba265072a02547f18a3b83dee5fa93a9"
SRCREV_meta_pn-linux-yocto_crownbay-noemgd ?= "82140b960a7cc13d116be61a85d4fe7f7d38680f"
