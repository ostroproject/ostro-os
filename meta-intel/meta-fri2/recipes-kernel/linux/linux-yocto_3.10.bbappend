FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2 = "fri2"
KBRANCH_fri2 = "standard/fri2"
KERNEL_FEATURES_append_fri2 = " features/drm-emgd/drm-emgd-1.18 cfg/vesafb"
LINUX_VERSION_fri2 = "3.10.38"
SRCREV_meta_fri2 = "617c6158c3d5b931f0d6131e0b0a7b374c792599"
SRCREV_machine_fri2 = "02f7e63e56c061617957388c23bd5cf9b05c5388"
SRCREV_emgd_fri2 = "42d5e4548e8e79e094fa8697949eed4cf6af00a3"
SRC_URI_fri2 = "git://git.yoctoproject.org/linux-yocto-3.10.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.18;name=machine,meta,emgd"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
KBRANCH_fri2-noemgd = "standard/fri2"
KERNEL_FEATURES_append_fri2-noemgd = " cfg/vesafb"
LINUX_VERSION_fri2-noemgd = "3.10.38"
SRCREV_meta_fri2-noemgd = "617c6158c3d5b931f0d6131e0b0a7b374c792599"
SRCREV_machine_fri2-noemgd = "02f7e63e56c061617957388c23bd5cf9b05c5388"

module_autoload_iwlwifi = "iwlwifi"

