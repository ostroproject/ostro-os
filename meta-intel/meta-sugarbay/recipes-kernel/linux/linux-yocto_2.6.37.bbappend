FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_sugarbay = "sugarbay"
KMACHINE_sugarbay  = "yocto/standard/common-pc-64/sugarbay"

SRCREV_machine_pn-linux-yocto_sugarbay ?= "7f495be2ccaa209bf505b8a8899cea64cfd968bb"
SRCREV_meta_pn-linux-yocto_sugarbay ?= "d5d3c6480d61f83503ccef7fbcd765f7aca8b71b"
