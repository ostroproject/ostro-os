FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

LINUX_VERSION = "3.8.13"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2 = "fri2"
KBRANCH_fri2 = "standard/fri2"
KERNEL_FEATURES_fri2_append = " features/drm-emgd/drm-emgd-1.16 cfg/vesafb"
SRCREV_meta_fri2 = "acee86ed84e252f1c3af782cc3aa044aaa13e51a"
SRCREV_machine_fri2 = "1f973c0fc8eea9a8f9758f47cf689ba89dbe9a25"
SRCREV_emgd_fri2 = "dd4eb42f0bce51625218da43f77ee4fae179d835"
SRC_URI_fri2 = "git://git.yoctoproject.org/linux-yocto-3.8.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.16;name=machine,meta,emgd"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
KBRANCH_fri2-noemgd = "standard/fri2"
KERNEL_FEATURES_fri2_append = " cfg/vesafb"
SRCREV_meta_fri2-noemgd = "acee86ed84e252f1c3af782cc3aa044aaa13e51a"
SRCREV_machine_fri2-noemgd = "1f973c0fc8eea9a8f9758f47cf689ba89dbe9a25"

module_autoload_iwlwifi = "iwlwifi"

