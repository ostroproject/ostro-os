FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow = "emenlow"
KMACHINE_emenlow  = "emenlow"
KBRANCH_emenlow  = "standard/emenlow"

SRCREV_machine_pn-linux-yocto_emenlow ?= "d8178545bc69adf262620fcfa40dd8f8ef64ba14"
SRCREV_meta_pn-linux-yocto_emenlow ?= "68a635bf8dfb64b02263c1ac80c948647cc76d5f"

LINUX_VERSION = "3.4.11"
