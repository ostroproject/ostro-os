FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow = "emenlow"
KMACHINE_emenlow  = "yocto/standard/emenlow"
KERNEL_FEATURES_append_emenlow += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto_emenlow ?= "32b75bf072568eb3e4e8efdd5fec7b8b15725146"
SRCREV_meta_pn-linux-yocto_emenlow ?= "d05450e4aef02c1b7137398ab3a9f8f96da74f52"
