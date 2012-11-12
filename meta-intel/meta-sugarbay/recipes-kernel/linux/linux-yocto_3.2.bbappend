FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_sugarbay = "sugarbay"

KMACHINE_sugarbay  = "sugarbay"
KBRANCH_sugarbay  = "standard/default/common-pc-64/sugarbay"

SRCREV_machine_pn-linux-yocto_sugarbay ?= "${AUTOREV}"
SRCREV_meta_pn-linux-yocto_sugarbay ?= "${AUTOREV}"

KERNEL_FEATURES_append_sugarbay = " features/tmp/rc6"
