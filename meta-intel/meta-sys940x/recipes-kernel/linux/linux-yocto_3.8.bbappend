FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

KMETA = "meta"

COMPATIBLE_MACHINE_sys940x = "sys940x"
KMACHINE_sys940x = "sys940x"
KBRANCH_sys940x = "standard/sys940x"
KERNEL_FEATURES_sys940x = " features/drm-emgd/drm-emgd-1.16"

COMPATIBLE_MACHINE_sys940x-noemgd = "sys940x-noemgd"
KMACHINE_sys940x-noemgd = "sys940x"
KBRANCH_sys940x-noemgd = "standard/sys940x"
KERNEL_FEATURES_sys940x-noemgd = " cfg/vesafb"

LINUX_VERSION = "3.8.4"

SRCREV_meta_sys940x = "2a6d36e75ca0a121570a389d7bab76ec240cbfda"
SRCREV_machine_sys940x = "47aed0c17c1c55988198ad39f86ae88894c8e0a4"
SRCREV_emgd_sys940x = "c780732f175ff0ec866fac2130175876b519b576"

SRCREV_meta_sys940x-noemgd = "2a6d36e75ca0a121570a389d7bab76ec240cbfda"
SRCREV_machine_sys940x-noemgd = "47aed0c17c1c55988198ad39f86ae88894c8e0a4"

SRC_URI_sys940x = "git://git.yoctoproject.org/linux-yocto-3.8.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.16;name=machine,meta,emgd"
