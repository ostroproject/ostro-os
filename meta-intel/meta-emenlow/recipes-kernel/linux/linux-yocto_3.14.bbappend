FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow-noemgd = "emenlow-noemgd"
KMACHINE_emenlow-noemgd = "emenlow"
KBRANCH_emenlow-noemgd = "standard/emenlow"
KERNEL_FEATURES_append_emenlow-noemgd = " features/drm-gma500/drm-gma500"

LINUX_VERSION_emenlow-noemgd = "3.14.0"
SRCREV_machine_emenlow-noemgd = "144595ef6215a0febfb8ee7d0c9e4eb2eaf93d61"
SRCREV_meta_emenlow-noemgd = "ad5f23c47b299418a88f13b1e6f119602115804a"
