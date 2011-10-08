FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fishriver = "fishriver"
KMACHINE_fishriver  = "yocto/standard/fishriver"
KERNEL_FEATURES_append_fishriver += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto_fishriver ?= "764df531641ae223bc8c7abf95e09b2aa42a79e5"
SRCREV_meta_pn-linux-yocto_fishriver ?= "353d43d340e87996b4be4c5f6ddb4447e050b65c"
