FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

LINUX_VERSION = "3.8.4"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2 = "fri2"
KBRANCH_fri2 = "standard/fri2"
KERNEL_FEATURES_fri2_append = " features/drm-emgd/drm-emgd-1.16 cfg/vesafb"
SRCREV_meta_fri2 = "2a6d36e75ca0a121570a389d7bab76ec240cbfda"
SRCREV_machine_fri2 = "47aed0c17c1c55988198ad39f86ae88894c8e0a4"
SRCREV_emgd_fri2 = "c780732f175ff0ec866fac2130175876b519b576"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
KBRANCH_fri2-noemgd = "standard/fri2"
KERNEL_FEATURES_fri2_append = " cfg/vesafb"
SRCREV_meta_fri2-noemgd = "2a6d36e75ca0a121570a389d7bab76ec240cbfda"
SRCREV_machine_fri2-noemgd = "47aed0c17c1c55988198ad39f86ae88894c8e0a4"

module_autoload_iwlwifi = "iwlwifi"

SRC_URI_fri2 = "git://git.yoctoproject.org/linux-yocto-3.8.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.16;name=machine,meta,emgd"
