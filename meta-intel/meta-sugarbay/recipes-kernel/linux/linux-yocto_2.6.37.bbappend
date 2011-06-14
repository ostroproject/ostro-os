FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_sugarbay = "sugarbay"
KMACHINE_sugarbay  = "yocto/standard/common-pc-64/sugarbay"

SRCREV_machine_pn-linux-yocto_sugarbay ?= "5021040d4d881cd0f4a741c6342a290a3af7d021"
SRCREV_meta_pn-linux-yocto_sugarbay ?= "f1dc3722d45cdcc92c84ebfecf4ce616d2efed26"
