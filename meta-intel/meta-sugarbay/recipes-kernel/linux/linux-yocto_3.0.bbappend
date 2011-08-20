FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_sugarbay = "sugarbay"
KMACHINE_sugarbay  = "yocto/standard/common-pc-64/sugarbay"

SRCREV_machine_pn-linux-yocto_sugarbay ?= "6f4f262873ffe7d4bde8f974af1c62fbfc07f17f"
SRCREV_meta_pn-linux-yocto_sugarbay ?= "d588bdafc0d9b4d2386144b7d76a1d379e2d16c0"
