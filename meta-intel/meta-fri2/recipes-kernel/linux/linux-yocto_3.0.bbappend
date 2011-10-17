FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2  = "yocto/standard/fri2"
KERNEL_FEATURES_append_fri2 += " cfg/smp.scc"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd  = "yocto/standard/fri2"
KERNEL_FEATURES_append_fri2-noemgd += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto_fri2 ?= "382ac4f36ebb34185b7cfa8ad74752ffcbe13993"
SRCREV_meta_pn-linux-yocto_fri2 ?= "353d43d340e87996b4be4c5f6ddb4447e050b65c"

SRCREV_machine_pn-linux-yocto_fri2-noemgd ?= "382ac4f36ebb34185b7cfa8ad74752ffcbe13993"
SRCREV_meta_pn-linux-yocto_fri2-noemgd ?= "353d43d340e87996b4be4c5f6ddb4447e050b65c"
