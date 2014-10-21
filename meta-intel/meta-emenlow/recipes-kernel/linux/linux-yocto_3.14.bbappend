FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow-noemgd = "emenlow-noemgd"
KMACHINE_emenlow-noemgd = "emenlow"
KBRANCH_emenlow-noemgd = "standard/base"
KERNEL_FEATURES_append_emenlow-noemgd = " features/drm-gma500/drm-gma500"

LINUX_VERSION_emenlow-noemgd = "3.14.19"
SRCREV_machine_emenlow-noemgd = "902f34d36102a4b2008b776ecae686f80d307e12"
SRCREV_meta_emenlow-noemgd = "28e39741b8b3018334021d981369d3fd61f18f5b"
