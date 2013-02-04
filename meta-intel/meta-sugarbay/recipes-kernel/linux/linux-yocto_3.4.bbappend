FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_sugarbay = "sugarbay"

KMACHINE_sugarbay  = "sugarbay"
KBRANCH_sugarbay  = "standard/common-pc-64/sugarbay"

SRCREV_machine_pn-linux-yocto_sugarbay ?= "13809f2cfd9be0ce86bd486e1643f9b90bed6f4f"
SRCREV_meta_pn-linux-yocto_sugarbay ?= "f697e099bc76d5df3a307a5bc0cc25021dd6dfe0"

LINUX_VERSION = "3.4.28"
