FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow-noemgd = "emenlow-noemgd"
KMACHINE_emenlow-noemgd = "emenlow"
KBRANCH_emenlow-noemgd = "standard/base"
KERNEL_FEATURES_append_emenlow-noemgd = " features/drm-gma500/drm-gma500"

LINUX_VERSION_emenlow-noemgd = "3.14.4"
SRCREV_machine_emenlow-noemgd = "cb22733185cd9db3e8945dadb899d9eb3831b9ad"
SRCREV_meta_emenlow-noemgd = "62f236c734996f240d91daee2cb6a05669c7326c"
