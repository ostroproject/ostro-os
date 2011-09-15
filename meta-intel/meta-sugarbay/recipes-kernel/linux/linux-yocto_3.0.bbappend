FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_sugarbay = "sugarbay"
KMACHINE_sugarbay  = "yocto/standard/common-pc-64/sugarbay"

SRCREV_machine_pn-linux-yocto_sugarbay ?= "dbe820c277dfa6cbc249d410e8b083286ec484b7"
SRCREV_meta_pn-linux-yocto_sugarbay ?= "12574e5a77597f6938315ef82d18fc5e229fb79c"
