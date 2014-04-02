FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"


COMPATIBLE_MACHINE_emenlow = "emenlow"
KMACHINE_emenlow = "emenlow"
KBRANCH_emenlow = "standard/emenlow"
KERNEL_FEATURES_append_emenlow = " features/drm-emgd/drm-emgd-1.18 cfg/vesafb"

COMPATIBLE_MACHINE_emenlow-noemgd = "emenlow-noemgd"
KMACHINE_emenlow-noemgd = "emenlow"
KBRANCH_emenlow-noemgd = "standard/emenlow"
KERNEL_FEATURES_append_emenlow-noemgd = " features/drm-gma500/drm-gma500"

LINUX_VERSION_emenlow = "3.10.35"
SRCREV_meta_emenlow = "b6e58b33dd427fe471f8827c83e311acdf4558a4"
SRCREV_machine_emenlow = "cee957655fe67826b2e827e2db41f156fa8f0cc4"
SRCREV_emgd_emenlow = "42d5e4548e8e79e094fa8697949eed4cf6af00a3"

LINUX_VERSION_emenlow-noemgd = "3.10.35"
SRCREV_meta_emenlow-noemgd = "b6e58b33dd427fe471f8827c83e311acdf4558a4"
SRCREV_machine_emenlow-noemgd = "cee957655fe67826b2e827e2db41f156fa8f0cc4"

SRC_URI_emenlow = "git://git.yoctoproject.org/linux-yocto-3.10.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.18;name=machine,meta,emgd"
