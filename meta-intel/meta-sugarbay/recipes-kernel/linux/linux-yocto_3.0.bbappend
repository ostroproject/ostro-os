FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_sugarbay = "sugarbay"
KMACHINE_sugarbay  = "yocto/standard/common-pc-64/sugarbay"

SRCREV_machine_pn-linux-yocto_sugarbay ?= "a52fb6e9ff9328dce8335db6c5891d0c4670d217"
SRCREV_meta_pn-linux-yocto_sugarbay ?= "67ce7623909cef63927fd145026aaf371cf4abf1"
