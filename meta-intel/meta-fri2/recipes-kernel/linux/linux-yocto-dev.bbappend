FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2 = "fri2"
KBRANCH_fri2 = "standard/fri2"
KERNEL_FEATURES_append_fri2 = " features/drm-emgd/drm-emgd-1.16 cfg/vesafb"
SRCREV_machine_fri2 = "60536206ad300ccf5b2be2c2d449f4ab27170238"
SRCREV_meta_fri2 = "fe20c99783387dab779472ff50a88666da1c6391"
SRCREV_emgd_fri2 = "17aacd908ed6035213a6d206cfdb2c0c9fa9e0c1"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
KBRANCH_fri2-noemgd = "standard/fri2"
KERNEL_FEATURES_append_fri2-noemgd = " cfg/vesafb"
SRCREV_machine_fri2-noemgd = "60536206ad300ccf5b2be2c2d449f4ab27170238"
SRCREV_meta_fri2-noemgd = "fe20c99783387dab779472ff50a88666da1c6391"

module_autoload_iwlwifi = "iwlwifi"

SRC_URI_fri2 = "git://git.yoctoproject.org/linux-yocto-dev.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.16;name=machine,meta,emgd"
