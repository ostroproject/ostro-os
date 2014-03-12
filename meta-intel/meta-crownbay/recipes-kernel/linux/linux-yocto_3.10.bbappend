FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"


COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay = "crownbay"
KBRANCH_crownbay = "standard/crownbay"
KERNEL_FEATURES_append_crownbay = " features/drm-emgd/drm-emgd-1.18 cfg/vesafb"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd = "crownbay"
KBRANCH_crownbay-noemgd = "standard/crownbay"
KERNEL_FEATURES_append_crownbay-noemgd = " cfg/vesafb"

LINUX_VERSION = "3.10.32"

SRCREV_meta_crownbay = "6e0e756d51372c8b176c5d1e6f786545bceed351"
SRCREV_machine_crownbay = "78afd3095c9b37efbbfbfdc25eb3833ef3c6a718"
SRCREV_emgd_crownbay = "42d5e4548e8e79e094fa8697949eed4cf6af00a3"

SRCREV_meta_crownbay-noemgd = "6e0e756d51372c8b176c5d1e6f786545bceed351"
SRCREV_machine_crownbay-noemgd = "78afd3095c9b37efbbfbfdc25eb3833ef3c6a718"

SRC_URI_crownbay = "git://git.yoctoproject.org/linux-yocto-3.10.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.18;name=machine,meta,emgd"
