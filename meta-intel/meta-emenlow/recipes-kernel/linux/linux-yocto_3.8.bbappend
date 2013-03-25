FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow = "emenlow"
KMACHINE_emenlow = "emenlow"
KBRANCH_emenlow = "standard/emenlow"
KERNEL_FEATURES_emenlow_append = " features/drm-emgd/drm-emgd-1.16 cfg/vesafb"

COMPATIBLE_MACHINE_emenlow-noemgd = "emenlow-noemgd"
KMACHINE_emenlow-noemgd = "emenlow"
KBRANCH_emenlow-noemgd = "standard/emenlow"
KERNEL_FEATURES_emenlow-noemgd_append = " features/drm-gma500/drm-gma600"

LINUX_VERSION = "3.8.4"

SRCREV_meta_emenlow = "2a6d36e75ca0a121570a389d7bab76ec240cbfda"
SRCREV_machine_emenlow = "47aed0c17c1c55988198ad39f86ae88894c8e0a4"
SRCREV_emgd_emenlow = "c780732f175ff0ec866fac2130175876b519b576"

SRCREV_meta_emenlow-noemgd = "2a6d36e75ca0a121570a389d7bab76ec240cbfda"
SRCREV_machine_emenlow-noemgd = "47aed0c17c1c55988198ad39f86ae88894c8e0a4"

SRC_URI_emenlow = "git://git.yoctoproject.org/linux-yocto-3.8.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.16;name=machine,meta,emgd"
