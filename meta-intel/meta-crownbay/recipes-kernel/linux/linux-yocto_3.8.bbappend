FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay = "crownbay"
KBRANCH_crownbay = "standard/crownbay"
KERNEL_FEATURES_crownbay_append = " features/drm-emgd/drm-emgd-1.16 cfg/vesafb"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd = "crownbay"
KBRANCH_crownbay-noemgd = "standard/crownbay"
KERNEL_FEATURES_crownbay-noemgd_append = " cfg/vesafb"

LINUX_VERSION = "3.8.11"

SRCREV_meta_crownbay = "edd6461602f6c2fc27bc72997e4437f422a9dccd"
SRCREV_machine_crownbay = "6ed6ca790b7afef5881de4566850bbc30ae26df6"
SRCREV_emgd_crownbay = "c780732f175ff0ec866fac2130175876b519b576"

SRCREV_meta_crownbay-noemgd = "edd6461602f6c2fc27bc72997e4437f422a9dccd"
SRCREV_machine_crownbay-noemgd = "6ed6ca790b7afef5881de4566850bbc30ae26df6"

SRC_URI_crownbay = "git://git.yoctoproject.org/linux-yocto-3.8.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.16;name=machine,meta,emgd"
