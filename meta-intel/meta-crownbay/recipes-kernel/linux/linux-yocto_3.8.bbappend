FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay = "crownbay"
KBRANCH_crownbay = "standard/crownbay"
KERNEL_FEATURES_crownbay_append = " features/drm-emgd/drm-emgd-1.16 cfg/vesafb"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd = "crownbay"
KBRANCH_crownbay-noemgd = "standard/crownbay"
KERNEL_FEATURES_crownbay-noemgd_append = " cfg/vesafb"

LINUX_VERSION = "3.8.4"

SRCREV_meta_crownbay = "2a6d36e75ca0a121570a389d7bab76ec240cbfda"
SRCREV_machine_crownbay = "47aed0c17c1c55988198ad39f86ae88894c8e0a4"
SRCREV_emgd_crownbay = "c780732f175ff0ec866fac2130175876b519b576"

SRCREV_meta_crownbay-noemgd = "2a6d36e75ca0a121570a389d7bab76ec240cbfda"
SRCREV_machine_crownbay-noemgd = "47aed0c17c1c55988198ad39f86ae88894c8e0a4"

SRC_URI_crownbay = "git://git.yoctoproject.org/linux-yocto-3.8.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.16;name=machine,meta,emgd"
