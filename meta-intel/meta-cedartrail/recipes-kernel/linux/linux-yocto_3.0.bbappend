FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_cedartrail = "cedartrail"
KMACHINE_cedartrail  = "yocto/standard/cedartrail"
KERNEL_FEATURES_append_cedartrail += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto_cedartrail ?= "153cb7313697f6638109ed6ce40009af353eeb94"
SRCREV_meta_pn-linux-yocto_cedartrail ?= "67ce7623909cef63927fd145026aaf371cf4abf1"
