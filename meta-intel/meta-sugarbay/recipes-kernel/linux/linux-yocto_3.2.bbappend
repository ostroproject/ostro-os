FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_sugarbay = "sugarbay"

KMACHINE_sugarbay  = "sugarbay"
KBRANCH_sugarbay  = "standard/default/common-pc-64/sugarbay"

SRCREV_machine_pn-linux-yocto_sugarbay ?= "0fe6d5d97c0a8d9e47716cb0da619deca07197e3"
SRCREV_meta_pn-linux-yocto_sugarbay ?= "49f931bc294d5b6be60502bbd448cff5aa766235"

KERNEL_FEATURES_append_sugarbay = " features/tmp/rc6"
