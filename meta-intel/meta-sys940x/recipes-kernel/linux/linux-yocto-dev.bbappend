FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

KMETA = "meta"

COMPATIBLE_MACHINE_sys940x = "sys940x"
KMACHINE_sys940x = "sys940x"
KBRANCH_sys940x = "standard/sys940x"
KERNEL_FEATURES_sys940x = " features/drm-emgd/drm-emgd-1.16"

COMPATIBLE_MACHINE_sys940x-noemgd = "sys940x-noemgd"
KMACHINE_sys940x-noemgd = "sys940x"
KBRANCH_sys940x-noemgd = "standard/sys940x"
KERNEL_FEATURES_sys940x-noemgd = " cfg/vesafb"

SRCREV_machine_sys940x = "60536206ad300ccf5b2be2c2d449f4ab27170238"
SRCREV_meta_sys940x = "fe20c99783387dab779472ff50a88666da1c6391"
SRCREV_emgd_sys940x = "17aacd908ed6035213a6d206cfdb2c0c9fa9e0c1"

SRCREV_machine_sys940x-noemgd = "60536206ad300ccf5b2be2c2d449f4ab27170238"
SRCREV_meta_sys940x-noemgd = "fe20c99783387dab779472ff50a88666da1c6391"

SRC_URI_sys940x = "git://git.yoctoproject.org/linux-yocto-dev.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.16;name=machine,meta,emgd"
