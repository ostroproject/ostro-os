FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow = "emenlow"
KMACHINE_emenlow  = "emenlow"
KBRANCH_emenlow  = "standard/default/emenlow"
KERNEL_FEATURES_append_emenlow += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto_emenlow ?= "86d05af47be45c786c1823a76b6854fa8b411bec"
SRCREV_meta_pn-linux-yocto_emenlow ?= "514847185c78c07f52e02750fbe0a03ca3a31d8f"
