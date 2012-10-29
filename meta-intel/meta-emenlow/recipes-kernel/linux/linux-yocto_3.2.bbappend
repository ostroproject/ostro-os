FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow = "emenlow"
KMACHINE_emenlow  = "emenlow"
KBRANCH_emenlow  = "standard/default/emenlow"

SRCREV_machine_pn-linux-yocto_emenlow ?= "9432e99fb8ca08b0d713fc4001f0b4a11138d20e"
SRCREV_meta_pn-linux-yocto_emenlow ?= "486f7aec824b4127e91ef53228823e996b3696f0"

LINUX_VERSION = "3.2.18"
