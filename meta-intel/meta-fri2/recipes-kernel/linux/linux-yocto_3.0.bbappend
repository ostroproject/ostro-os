FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2  = "yocto/standard/fri2"
KERNEL_FEATURES_append_fri2 += " cfg/smp.scc"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd  = "yocto/standard/fri2"
KERNEL_FEATURES_append_fri2-noemgd += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto_fri2 ?= "382ac4f36ebb34185b7cfa8ad74752ffcbe13993"
SRCREV_meta_pn-linux-yocto_fri2 ?= "334b8479297954d94c97f81164e3363ed7ae70e5"

SRCREV_machine_pn-linux-yocto_fri2-noemgd ?= "382ac4f36ebb34185b7cfa8ad74752ffcbe13993"
SRCREV_meta_pn-linux-yocto_fri2-noemgd ?= "334b8479297954d94c97f81164e3363ed7ae70e5"
