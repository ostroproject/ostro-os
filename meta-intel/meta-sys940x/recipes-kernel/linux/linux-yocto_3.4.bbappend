FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"


KMETA = "meta"

COMPATIBLE_MACHINE_sys940x = "sys940x"
KMACHINE_sys940x  = "sys940x"
KBRANCH_sys940x  = "standard/base"
KERNEL_FEATURES_sys940x = " features/drm-emgd/drm-emgd-1.16"

COMPATIBLE_MACHINE_sys940x-noemgd = "sys940x-noemgd"
KMACHINE_sys940x-noemgd  = "sys940x"
KBRANCH_sys940x-noemgd  = "standard/base"
KERNEL_FEATURES_sys940x-noemgd = " cfg/vesafb"

SRCREV_machine_pn-linux-yocto_sys940x ?= "13809f2cfd9be0ce86bd486e1643f9b90bed6f4f"
SRCREV_meta_pn-linux-yocto_sys940x ?= "f697e099bc76d5df3a307a5bc0cc25021dd6dfe0"
SRCREV_emgd_pn-linux-yocto_sys940x ?= "86643bdd8cbad616a161ab91f51108cf0da827bc"

SRCREV_machine_pn-linux-yocto_sys940x-noemgd ?= "13809f2cfd9be0ce86bd486e1643f9b90bed6f4f"
SRCREV_meta_pn-linux-yocto_sys940x-noemgd ?= "f697e099bc76d5df3a307a5bc0cc25021dd6dfe0"

SRC_URI_sys940x = "git://git.yoctoproject.org/linux-yocto-3.4.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.16;name=machine,meta,emgd"

LINUX_VERSION = "3.4.28"
