FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_sugarbay = "sugarbay"
KMACHINE_sugarbay  = "yocto/standard/common-pc-64/sugarbay"

SRCREV_machine_pn-linux-yocto_sugarbay ?= "dbe820c277dfa6cbc249d410e8b083286ec484b7"
SRCREV_meta_pn-linux-yocto_sugarbay ?= "353d43d340e87996b4be4c5f6ddb4447e050b65c"
