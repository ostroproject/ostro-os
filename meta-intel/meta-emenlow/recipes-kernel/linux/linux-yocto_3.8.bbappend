FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow = "emenlow"
KMACHINE_emenlow = "emenlow"
KBRANCH_emenlow = "standard/emenlow"
KERNEL_FEATURES_emenlow_append = " features/drm-emgd/drm-emgd-1.16 cfg/vesafb"

COMPATIBLE_MACHINE_emenlow-noemgd = "emenlow-noemgd"
KMACHINE_emenlow-noemgd = "emenlow"
KBRANCH_emenlow-noemgd = "standard/emenlow"
KERNEL_FEATURES_emenlow-noemgd_append = " features/drm-gma500/drm-gma600"

LINUX_VERSION = "3.8.11"

SRCREV_meta_emenlow = "edd6461602f6c2fc27bc72997e4437f422a9dccd"
SRCREV_machine_emenlow = "6ed6ca790b7afef5881de4566850bbc30ae26df6"
SRCREV_emgd_emenlow = "c780732f175ff0ec866fac2130175876b519b576"

SRCREV_meta_emenlow-noemgd = "edd6461602f6c2fc27bc72997e4437f422a9dccd"
SRCREV_machine_emenlow-noemgd = "6ed6ca790b7afef5881de4566850bbc30ae26df6"

SRC_URI_emenlow = "git://git.yoctoproject.org/linux-yocto-3.8.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.16;name=machine,meta,emgd"
