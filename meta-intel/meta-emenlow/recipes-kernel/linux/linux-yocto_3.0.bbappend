FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow = "emenlow"
KMACHINE_emenlow  = "emenlow"
KBRANCH_emenlow  = "yocto/standard/emenlow"
KERNEL_FEATURES_append_emenlow += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto_emenlow ?= "0b13bbbc423fea345fd537792284ccf388809e5b"
SRCREV_meta_pn-linux-yocto_emenlow ?= "59314a3523e360796419d76d78c6f7d8c5ef2593"
