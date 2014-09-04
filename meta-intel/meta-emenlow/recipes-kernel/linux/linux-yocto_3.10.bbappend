FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow-noemgd = "emenlow-noemgd"
KMACHINE_emenlow-noemgd = "emenlow"
KBRANCH_emenlow-noemgd = "standard/emenlow"
KERNEL_FEATURES_append_emenlow-noemgd = " features/drm-gma500/drm-gma500"

LINUX_VERSION_emenlow-noemgd = "3.10.38"
SRCREV_meta_emenlow-noemgd = "e1f26aeccfd43bc3d7e95873ceda469b631b8473"
SRCREV_machine_emenlow-noemgd = "02f7e63e56c061617957388c23bd5cf9b05c5388"
