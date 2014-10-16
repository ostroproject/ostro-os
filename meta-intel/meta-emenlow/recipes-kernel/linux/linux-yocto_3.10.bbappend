FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow-noemgd = "emenlow-noemgd"
KMACHINE_emenlow-noemgd = "emenlow"
KBRANCH_emenlow-noemgd = "standard/emenlow"
KERNEL_FEATURES_append_emenlow-noemgd = " features/drm-gma500/drm-gma500"

LINUX_VERSION_emenlow-noemgd = "3.10.55"
SRCREV_meta_emenlow-noemgd = "f79a00265eefbe2fffc2cdb03f67235497a9a87e"
SRCREV_machine_emenlow-noemgd = "3677ea7f9476458aa6dec440243de3a6fb1343a9"
