FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow = "emenlow"
KMACHINE_emenlow  = "yocto/standard/emenlow"
KERNEL_FEATURES_append_emenlow += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto_emenlow ?= "32b75bf072568eb3e4e8efdd5fec7b8b15725146"
SRCREV_meta_pn-linux-yocto_emenlow ?= "0dcdf7bb40a8e1fb18fd27d442fa5ace8cff4941"
