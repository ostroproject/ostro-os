FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_sugarbay = "sugarbay"

KMACHINE_sugarbay  = "sugarbay"
KBRANCH_sugarbay  = "standard/default/common-pc-64/sugarbay"

SRCREV_machine_pn-linux-yocto_sugarbay ?= "1c0a82537cef285d35a1bce112895f135b8272ae"
SRCREV_meta_pn-linux-yocto_sugarbay ?= "e7f2fdc48f8808887175f0328274a2668084738c"

KERNEL_FEATURES_append_sugarbay = " features/tmp/rc6"

LINUX_VERSION = "3.2.32"
