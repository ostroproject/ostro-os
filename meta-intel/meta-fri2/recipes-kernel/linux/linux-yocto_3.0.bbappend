FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2  = "yocto/standard/fri2"
KERNEL_FEATURES_append_fri2 += " cfg/smp.scc"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd  = "yocto/standard/fri2"
KERNEL_FEATURES_append_fri2-noemgd += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto_fri2 ?= "f1167dd736c4a4aea834b853d73c51f9863151b4"
SRCREV_meta_pn-linux-yocto_fri2 ?= "5b535279e61197cb194bb2dfceb8b7a04128387c"

SRCREV_machine_pn-linux-yocto_fri2-noemgd ?= "f1167dd736c4a4aea834b853d73c51f9863151b4"
SRCREV_meta_pn-linux-yocto_fri2-noemgd ?= "5b535279e61197cb194bb2dfceb8b7a04128387c"
