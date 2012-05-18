FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fishriver = "fishriver"
KMACHINE_fishriver  = "fishriver"
KBRANCH_fishriver  = "yocto/standard/fishriver"
KERNEL_FEATURES_append_fishriver += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto_fishriver ?= "c139592c96722727a9f074515a4061c3820da1a6"
SRCREV_meta_pn-linux-yocto_fishriver ?= "59314a3523e360796419d76d78c6f7d8c5ef2593"
