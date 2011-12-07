FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2  = "yocto/standard/fri2"
KERNEL_FEATURES_append_fri2 += " cfg/smp.scc cfg/efi-ext.scc"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd  = "yocto/standard/fri2"
KERNEL_FEATURES_append_fri2-noemgd += " cfg/smp.scc cfg/efi-ext.scc"

SRCREV_machine_pn-linux-yocto_fri2 ?= "20507c447f92907a6df53bc4f03655f050367ec7"
SRCREV_meta_pn-linux-yocto_fri2 ?= "67ce7623909cef63927fd145026aaf371cf4abf1"

SRCREV_machine_pn-linux-yocto_fri2-noemgd ?= "20507c447f92907a6df53bc4f03655f050367ec7"
SRCREV_meta_pn-linux-yocto_fri2-noemgd ?= "67ce7623909cef63927fd145026aaf371cf4abf1"
