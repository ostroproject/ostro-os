FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow = "emenlow"
KMACHINE_emenlow  = "emenlow"
KBRANCH_emenlow  = "standard/emenlow"
KERNEL_FEATURES_emenlow_append = " features/drm-emgd/drm-emgd-1.16 cfg/vesafb"

COMPATIBLE_MACHINE_emenlow-noemgd = "emenlow-noemgd"
KMACHINE_emenlow-noemgd  = "emenlow"
KBRANCH_emenlow-noemgd  = "standard/emenlow"
KERNEL_FEATURES_emenlow-noemgd_append = " features/drm-gma500/drm-gma600"

SRCREV_machine_pn-linux-yocto_emenlow ?= "${AUTOREV}"
SRCREV_meta_pn-linux-yocto_emenlow ?= "${AUTOREV}"
SRCREV_emgd_pn-linux-yocto_emenlow ?= "${AUTOREV}"

SRCREV_machine_pn-linux-yocto_emenlow-noemgd ?= "${AUTOREV}"
SRCREV_meta_pn-linux-yocto_emenlow-noemgd ?= "${AUTOREV}"

SRC_URI_emenlow = "git://git.yoctoproject.org/linux-yocto-3.4.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.16;name=machine,meta,emgd"
