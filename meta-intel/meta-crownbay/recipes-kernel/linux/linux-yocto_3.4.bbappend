FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"


COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay  = "crownbay"
KBRANCH_crownbay  = "standard/crownbay"
KERNEL_FEATURES_append_crownbay= " features/drm-emgd/drm-emgd-1.16 cfg/vesafb"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd  = "crownbay"
KBRANCH_crownbay-noemgd  = "standard/crownbay"
KERNEL_FEATURES_append_crownbay-noemgd = " cfg/vesafb"

SRCREV_machine_pn-linux-yocto_crownbay ?= "de0c0ed674dfdbd808657e299fc720d8a97cb868"
SRCREV_meta_pn-linux-yocto_crownbay ?= "9473a39c59bf9c07a316486d272652bacb9ad3ac"
SRCREV_emgd_pn-linux-yocto_crownbay ?= "f5c3a221f0e42d48ee5af369d73594e26ef7fae6"

SRCREV_machine_pn-linux-yocto_crownbay-noemgd ?= "de0c0ed674dfdbd808657e299fc720d8a97cb868"
SRCREV_meta_pn-linux-yocto_crownbay-noemgd ?= "9473a39c59bf9c07a316486d272652bacb9ad3ac"

SRC_URI_crownbay = "git://git.yoctoproject.org/linux-yocto-3.4.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA},emgd-1.16;name=machine,meta,emgd"
SRC_URI_crownbay-noemgd = "git://git.yoctoproject.org/linux-yocto-3.4.git;protocol=git;nocheckout=1;branch=${KBRANCH},${KMETA};name=machine,meta"

LINUX_VERSION = "3.4.46"
