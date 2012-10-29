FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_sugarbay = "sugarbay"

KMACHINE_sugarbay  = "sugarbay"
KBRANCH_sugarbay  = "standard/default/common-pc-64/sugarbay"

SRCREV_machine_pn-linux-yocto_sugarbay ?= "1b6466421bc314e7e07fe4dd48c5fc67cdc3fc40"
SRCREV_meta_pn-linux-yocto_sugarbay ?= "486f7aec824b4127e91ef53228823e996b3696f0"

LINUX_VERSION = "3.2.18"

KERNEL_FEATURES_append_sugarbay = " features/tmp/rc6"
