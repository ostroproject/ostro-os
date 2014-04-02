FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow-noemgd = "emenlow-noemgd"
KMACHINE_emenlow-noemgd = "emenlow"
KBRANCH_emenlow-noemgd = "standard/emenlow"
KERNEL_FEATURES_append_emenlow-noemgd = " features/drm-gma500/drm-gma500"

LINUX_VERSION_emenlow-noemgd = "3.14.0"
SRCREV_machine_emenlow-noemgd = "0143c6ebb4a2d63b241df5f608b19f483f7eb9e0"
SRCREV_meta_emenlow-noemgd = "fc8c30398dbc3cdea787a1042242d4aab689d0ae"
