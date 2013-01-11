FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow = "emenlow"
KMACHINE_emenlow  = "emenlow"
KBRANCH_emenlow  = "standard/emenlow"
KERNEL_FEATURES_emenlow_append = " features/drm-emgd cfg/vesafb"

SRCREV_machine_pn-linux-yocto_emenlow ?= "${AUTOREV}"
SRCREV_meta_pn-linux-yocto_emenlow ?= "${AUTOREV}"
