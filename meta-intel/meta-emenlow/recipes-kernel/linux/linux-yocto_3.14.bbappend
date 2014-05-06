FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow-noemgd = "emenlow-noemgd"
KMACHINE_emenlow-noemgd = "emenlow"
KBRANCH_emenlow-noemgd = "standard/emenlow"
KERNEL_FEATURES_append_emenlow-noemgd = " features/drm-gma500/drm-gma500"

LINUX_VERSION_emenlow-noemgd = "3.14.2"
SRCREV_machine_emenlow-noemgd = "b0b9c962ea01f9356fc1542b9696ebe4a38e196a"
SRCREV_meta_emenlow-noemgd = "4df1e2ed992adeac4da60ad5118d0237e8cb88df"
