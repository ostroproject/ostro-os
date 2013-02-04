FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow = "emenlow"
KMACHINE_emenlow  = "emenlow"
KBRANCH_emenlow  = "standard/default/emenlow"

SRCREV_machine_pn-linux-yocto_emenlow ?= "a0dbaa15a7b42122449c4069a55b6bc60b579ee7"
SRCREV_meta_pn-linux-yocto_emenlow ?= "e7f2fdc48f8808887175f0328274a2668084738c"

LINUX_VERSION = "3.2.32"
