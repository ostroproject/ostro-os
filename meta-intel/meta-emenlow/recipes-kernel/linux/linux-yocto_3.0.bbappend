FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow = "emenlow"
KMACHINE_emenlow  = "yocto/standard/emenlow"
KERNEL_FEATURES_append_emenlow += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto_emenlow ?= "ae00bcfe717db99ac2ff53f1ad995f589deffc53"
SRCREV_meta_pn-linux-yocto_emenlow ?= "67ce7623909cef63927fd145026aaf371cf4abf1"
