FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow = "emenlow"
KMACHINE_emenlow = "emenlow"
KBRANCH_emenlow = "standard/emenlow"
KERNEL_FEATURES_append_emenlow = " features/drm-emgd/drm-emgd-1.16 cfg/vesafb"

COMPATIBLE_MACHINE_emenlow-noemgd = "emenlow-noemgd"
KMACHINE_emenlow-noemgd = "emenlow"
KBRANCH_emenlow-noemgd = "standard/emenlow"
KERNEL_FEATURES_append_emenlow-noemgd = " features/drm-gma500/drm-gma500"

SRCREV_machine_emenlow = "60536206ad300ccf5b2be2c2d449f4ab27170238"
SRCREV_meta_emenlow = "fe20c99783387dab779472ff50a88666da1c6391"
SRCREV_emgd_emenlow = "17aacd908ed6035213a6d206cfdb2c0c9fa9e0c1"

SRCREV_machine_emenlow-noemgd = "60536206ad300ccf5b2be2c2d449f4ab27170238"
SRCREV_meta_emenlow-noemgd = "fe20c99783387dab779472ff50a88666da1c6391"

SRC_URI_emenlow = "git://git.yoctoproject.org/linux-yocto-dev.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.16;name=machine,meta,emgd"
