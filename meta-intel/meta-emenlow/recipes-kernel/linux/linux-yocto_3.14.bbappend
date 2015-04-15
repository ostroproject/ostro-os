FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow-noemgd = "emenlow-noemgd"
KMACHINE_emenlow-noemgd = "emenlow"
KBRANCH_emenlow-noemgd = "standard/base"
KERNEL_FEATURES_append_emenlow-noemgd = " features/drm-gma500/drm-gma500"

LINUX_VERSION_emenlow-noemgd = "3.14.36"
SRCREV_machine_emenlow-noemgd = "4434aa71ff7043c570f9eae493df1ccadbda9b85"
SRCREV_meta_emenlow-noemgd = "162dfe3bb092c1a792e5ed224fe09672e9814b24"
