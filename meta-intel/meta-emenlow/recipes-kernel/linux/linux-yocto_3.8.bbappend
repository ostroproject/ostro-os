FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow = "emenlow"
KMACHINE_emenlow = "emenlow"
KBRANCH_emenlow = "standard/emenlow"
KERNEL_FEATURES_emenlow_append = " features/drm-emgd/drm-emgd-1.16 cfg/vesafb"

COMPATIBLE_MACHINE_emenlow-noemgd = "emenlow-noemgd"
KMACHINE_emenlow-noemgd = "emenlow"
KBRANCH_emenlow-noemgd = "standard/emenlow"
KERNEL_FEATURES_emenlow-noemgd_append = " features/drm-gma500/drm-gma600"

LINUX_VERSION = "3.8.13"

SRCREV_meta_emenlow = "acee86ed84e252f1c3af782cc3aa044aaa13e51a"
SRCREV_machine_emenlow = "1f973c0fc8eea9a8f9758f47cf689ba89dbe9a25"
SRCREV_emgd_emenlow = "dd4eb42f0bce51625218da43f77ee4fae179d835"

SRCREV_meta_emenlow-noemgd = "acee86ed84e252f1c3af782cc3aa044aaa13e51a"
SRCREV_machine_emenlow-noemgd = "1f973c0fc8eea9a8f9758f47cf689ba89dbe9a25"

SRC_URI_emenlow = "git://git.yoctoproject.org/linux-yocto-3.8.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.16;name=machine,meta,emgd"
