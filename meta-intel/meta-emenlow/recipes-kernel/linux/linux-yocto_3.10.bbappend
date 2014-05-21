FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"


COMPATIBLE_MACHINE_emenlow = "emenlow"
KMACHINE_emenlow = "emenlow"
KBRANCH_emenlow = "standard/emenlow"
KERNEL_FEATURES_append_emenlow = " features/drm-emgd/drm-emgd-1.18 cfg/vesafb"

COMPATIBLE_MACHINE_emenlow-noemgd = "emenlow-noemgd"
KMACHINE_emenlow-noemgd = "emenlow"
KBRANCH_emenlow-noemgd = "standard/emenlow"
KERNEL_FEATURES_append_emenlow-noemgd = " features/drm-gma500/drm-gma500"

LINUX_VERSION_emenlow = "3.10.38"
SRCREV_meta_emenlow = "e1f26aeccfd43bc3d7e95873ceda469b631b8473"
SRCREV_machine_emenlow = "02f7e63e56c061617957388c23bd5cf9b05c5388"
SRCREV_emgd_emenlow = "42d5e4548e8e79e094fa8697949eed4cf6af00a3"

LINUX_VERSION_emenlow-noemgd = "3.10.38"
SRCREV_meta_emenlow-noemgd = "e1f26aeccfd43bc3d7e95873ceda469b631b8473"
SRCREV_machine_emenlow-noemgd = "02f7e63e56c061617957388c23bd5cf9b05c5388"

SRC_URI_emenlow = "git://git.yoctoproject.org/linux-yocto-3.10.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.18;name=machine,meta,emgd"
