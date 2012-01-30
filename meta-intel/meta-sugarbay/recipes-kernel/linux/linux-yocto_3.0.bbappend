FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_sugarbay = "sugarbay"
KMACHINE_sugarbay  = "yocto/standard/common-pc-64/sugarbay"

SRCREV_machine_pn-linux-yocto_sugarbay ?= "162abf381df130fbf6ba8df353821fa684e59dfa"
SRCREV_meta_pn-linux-yocto_sugarbay ?= "59314a3523e360796419d76d78c6f7d8c5ef2593"
