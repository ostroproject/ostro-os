FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow-noemgd = "emenlow-noemgd"
KMACHINE_emenlow-noemgd = "emenlow"
KBRANCH_emenlow-noemgd = "standard/emenlow"
KERNEL_FEATURES_append_emenlow-noemgd = " features/drm-gma500/drm-gma500"

LINUX_VERSION = "3.10.11"

SRCREV_meta_emenlow-noemgd = "285f93bf942e8f6fa678ffc6cc53696ed5400718"
SRCREV_machine_emenlow-noemgd = "702040ac7c7ec66a29b4d147665ccdd0ff015577"
