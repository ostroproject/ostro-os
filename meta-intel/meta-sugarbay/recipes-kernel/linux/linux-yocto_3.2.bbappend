FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_sugarbay = "sugarbay"

KMACHINE_sugarbay  = "sugarbay"
KBRANCH_sugarbay  = "standard/default/common-pc-64/sugarbay"

SRCREV_machine_pn-linux-yocto_sugarbay ?= "172df847dda93cb52af0c694200613a1c363c9a3"
SRCREV_meta_pn-linux-yocto_sugarbay ?= "5b4c9dc78b5ae607173cc3ddab9bce1b5f78129b"

KERNEL_FEATURES_append_sugarbay = " features/tmp/rc6"
