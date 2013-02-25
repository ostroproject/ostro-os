FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay = "crownbay"
KBRANCH_crownbay = "standard/crownbay"
KERNEL_FEATURES_crownbay_append = " features/drm-emgd/drm-emgd-1.16 cfg/vesafb"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd = "crownbay"
KBRANCH_crownbay-noemgd = "standard/crownbay"
KERNEL_FEATURES_crownbay-noemgd_append = " cfg/vesafb"

SRCREV_meta_crownbay = "fe20c99783387dab779472ff50a88666da1c6391"
SRCREV_machine_crownbay = "60536206ad300ccf5b2be2c2d449f4ab27170238"
SRCREV_emgd_crownbay = "17aacd908ed6035213a6d206cfdb2c0c9fa9e0c1"

SRCREV_machine_crownbay-noemgd = "60536206ad300ccf5b2be2c2d449f4ab27170238"
SRCREV_meta_crownbay-noemgd = "fe20c99783387dab779472ff50a88666da1c6391"

SRC_URI_crownbay = "git://git.yoctoproject.org/linux-yocto-dev.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.16;name=machine,meta,emgd"
