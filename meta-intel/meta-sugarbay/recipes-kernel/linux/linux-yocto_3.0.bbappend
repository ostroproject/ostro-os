FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_sugarbay = "sugarbay"
KMACHINE_sugarbay  = "yocto/standard/common-pc-64/sugarbay"

SRCREV_machine_pn-linux-yocto_sugarbay ?= "b0430dab0b3af4a12fe057cecc63ce98f9419ce1"
SRCREV_meta_pn-linux-yocto_sugarbay ?= "9da70812ecddee0f7eeb11675f29497cb997275e"
