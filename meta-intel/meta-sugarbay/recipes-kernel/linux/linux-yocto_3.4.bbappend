FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"


COMPATIBLE_MACHINE_sugarbay = "sugarbay"

KMACHINE_sugarbay  = "sugarbay"
KBRANCH_sugarbay  = "standard/common-pc-64/sugarbay"

SRCREV_machine_pn-linux-yocto_sugarbay ?= "de0c0ed674dfdbd808657e299fc720d8a97cb868"
SRCREV_meta_pn-linux-yocto_sugarbay ?= "9473a39c59bf9c07a316486d272652bacb9ad3ac"

LINUX_VERSION = "3.4.46"
