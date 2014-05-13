FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow-noemgd = "emenlow-noemgd"
KMACHINE_emenlow-noemgd = "emenlow"
KBRANCH_emenlow-noemgd = "standard/base"
KERNEL_FEATURES_append_emenlow-noemgd = " features/drm-gma500/drm-gma500"

LINUX_VERSION_emenlow-noemgd = "3.14.2"
SRCREV_machine_emenlow-noemgd = "b0b9c962ea01f9356fc1542b9696ebe4a38e196a"
SRCREV_meta_emenlow-noemgd = "71d5b64a173f51107bf947ceef80a5a7c8d72a7d"
