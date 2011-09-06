FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2  = "yocto/standard/fri2"
KERNEL_FEATURES_append_fri2 += " cfg/smp.scc"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd  = "yocto/standard/fri2"
KERNEL_FEATURES_append_fri2-noemgd += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto_fri2 ?= "05764d3cd8c87fd30f87f4e559c416e6e1c40fb3"
SRCREV_meta_pn-linux-yocto_fri2 ?= "82140b960a7cc13d116be61a85d4fe7f7d38680f"

SRCREV_machine_pn-linux-yocto_fri2-noemgd ?= "05764d3cd8c87fd30f87f4e559c416e6e1c40fb3"
SRCREV_meta_pn-linux-yocto_fri2-noemgd ?= "82140b960a7cc13d116be61a85d4fe7f7d38680f"
