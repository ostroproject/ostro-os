FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_sugarbay = "sugarbay"

KMACHINE_sugarbay  = "sugarbay"
KBRANCH_sugarbay  = "standard/common-pc-64/sugarbay"

SRCREV_machine_pn-linux-yocto_sugarbay ?= "218bd8d2022b9852c60d32f0d770931e3cf343e2"
SRCREV_meta_pn-linux-yocto_sugarbay ?= "68a635bf8dfb64b02263c1ac80c948647cc76d5f"

LINUX_VERSION = "3.4.11"
