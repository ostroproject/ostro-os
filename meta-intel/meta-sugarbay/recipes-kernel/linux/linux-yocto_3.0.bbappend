FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_sugarbay = "sugarbay"
KMACHINE_sugarbay  = "yocto/standard/common-pc-64/sugarbay"

SRCREV_machine_pn-linux-yocto_sugarbay ?= "2a4f677e3f9767515fac25e4c37c4af179beceba"
SRCREV_meta_pn-linux-yocto_sugarbay ?= "82140b960a7cc13d116be61a85d4fe7f7d38680f"
