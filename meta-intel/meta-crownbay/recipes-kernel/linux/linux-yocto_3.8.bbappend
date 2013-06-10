FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay = "crownbay"
KBRANCH_crownbay = "standard/crownbay"
KERNEL_FEATURES_crownbay_append = " features/drm-emgd/drm-emgd-1.16 cfg/vesafb"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd = "crownbay"
KBRANCH_crownbay-noemgd = "standard/crownbay"
KERNEL_FEATURES_crownbay-noemgd_append = " cfg/vesafb"

LINUX_VERSION = "3.8.13"

SRCREV_meta_crownbay = "acee86ed84e252f1c3af782cc3aa044aaa13e51a"
SRCREV_machine_crownbay = "1f973c0fc8eea9a8f9758f47cf689ba89dbe9a25"
SRCREV_emgd_crownbay = "dd4eb42f0bce51625218da43f77ee4fae179d835"

SRCREV_meta_crownbay-noemgd = "acee86ed84e252f1c3af782cc3aa044aaa13e51a"
SRCREV_machine_crownbay-noemgd = "1f973c0fc8eea9a8f9758f47cf689ba89dbe9a25"

SRC_URI_crownbay = "git://git.yoctoproject.org/linux-yocto-3.8.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.16;name=machine,meta,emgd"
