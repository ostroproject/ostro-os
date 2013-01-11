FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

KMETA = "meta"

COMPATIBLE_MACHINE_sys940x = "sys940x"
KMACHINE_sys940x  = "sys940x"
KBRANCH_sys940x  = "standard/base"
KERNEL_FEATURES_sys940x = " features/drm-emgd"

COMPATIBLE_MACHINE_sys940x-noemgd = "sys940x-noemgd"
KMACHINE_sys940x-noemgd  = "sys940x"
KBRANCH_sys940x-noemgd  = "standard/base"
KERNEL_FEATURES_sys940x-noemgd = " cfg/vesafb"

SRCREV_machine_pn-linux-yocto_sys940x ?= "${AUTOREV}"
SRCREV_meta_pn-linux-yocto_sys940x ?= "${AUTOREV}"
SRCREV_emgd_pn-linux-yocto_sys940x ?= "${AUTOREV}"

SRCREV_machine_pn-linux-yocto_sys940x-noemgd ?= "${AUTOREV}"
SRCREV_meta_pn-linux-yocto_sys940x-noemgd ?= "${AUTOREV}"

SRC_URI_sys940x = "git://${KSRC_linux_yocto_3_4_repo};nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.14;name=machine,meta,emgd"
