FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow = "emenlow"
KMACHINE_emenlow  = "emenlow"
KBRANCH_emenlow  = "standard/default/emenlow"
KERNEL_FEATURES_append_emenlow += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto_emenlow ?= "4ee2ae2967b59300f5acd18292688d34d6387f2e"
SRCREV_meta_pn-linux-yocto_emenlow ?= "b14a08f5c7b469a5077c10942f4e1aec171faa9d"
