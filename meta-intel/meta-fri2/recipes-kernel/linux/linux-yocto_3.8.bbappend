FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

LINUX_VERSION = "3.8.11"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2 = "fri2"
KBRANCH_fri2 = "standard/fri2"
KERNEL_FEATURES_fri2_append = " features/drm-emgd/drm-emgd-1.16 cfg/vesafb"
SRCREV_meta_fri2 = "edd6461602f6c2fc27bc72997e4437f422a9dccd"
SRCREV_machine_fri2 = "6ed6ca790b7afef5881de4566850bbc30ae26df6"
SRCREV_emgd_fri2 = "c780732f175ff0ec866fac2130175876b519b576"
SRC_URI_fri2 = "git://git.yoctoproject.org/linux-yocto-3.8.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.16;name=machine,meta,emgd"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
KBRANCH_fri2-noemgd = "standard/fri2"
KERNEL_FEATURES_fri2_append = " cfg/vesafb"
SRCREV_meta_fri2-noemgd = "edd6461602f6c2fc27bc72997e4437f422a9dccd"
SRCREV_machine_fri2-noemgd = "6ed6ca790b7afef5881de4566850bbc30ae26df6"

module_autoload_iwlwifi = "iwlwifi"

