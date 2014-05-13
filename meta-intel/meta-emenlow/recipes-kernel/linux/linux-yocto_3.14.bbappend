FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow-noemgd = "emenlow-noemgd"
KMACHINE_emenlow-noemgd = "emenlow"
KBRANCH_emenlow-noemgd = "standard/base"
KERNEL_FEATURES_append_emenlow-noemgd = " features/drm-gma500/drm-gma500"

LINUX_VERSION_emenlow-noemgd = "3.14.2"
SRCREV_machine_emenlow-noemgd = "d0047ab24e8e92fc2a116b0bccfa10d6b84985be"
SRCREV_meta_emenlow-noemgd = "11e091dc40c53af6ea08ce491ae50fbb1b0b6377"
