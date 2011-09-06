FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_sugarbay = "sugarbay"
KMACHINE_sugarbay  = "yocto/standard/common-pc-64/sugarbay"

SRCREV_machine_pn-linux-yocto_sugarbay ?= "dbe820c277dfa6cbc249d410e8b083286ec484b7"
SRCREV_meta_pn-linux-yocto_sugarbay ?= "3c9ebeed2598b74798a0c9247ef7c385e0cd96a7"
