FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow-noemgd = "emenlow-noemgd"
KMACHINE_emenlow-noemgd = "emenlow"
KBRANCH_emenlow-noemgd = "standard/emenlow"
KERNEL_FEATURES_append_emenlow-noemgd = " features/drm-gma500/drm-gma500"

LINUX_VERSION = "3.10.11"

SRCREV_meta_emenlow-noemgd = "363bd856c8101d4227d492cc911bc4ca0c4987c6"
SRCREV_machine_emenlow-noemgd = "e1aa804148370cda6f85640281af156ffa007d52"
