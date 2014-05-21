FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow-noemgd = "emenlow-noemgd"
KMACHINE_emenlow-noemgd = "emenlow"
KBRANCH_emenlow-noemgd = "standard/emenlow"
KERNEL_FEATURES_append_emenlow-noemgd = " features/drm-gma500/drm-gma500"

# NOTE: We do not set SRCREVs here as -dev is intended to be built with AUTOREV
# and setting them here breaks the default mechanism to use AUTOREV if the
# default SRCREV is set and linux-yocto-dev is the preferred provider.
