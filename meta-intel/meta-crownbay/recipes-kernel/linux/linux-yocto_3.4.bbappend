FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay  = "crownbay"
KBRANCH_crownbay  = "standard/default/crownbay"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd  = "crownbay"
KBRANCH_crownbay-noemgd  = "standard/crownbay"

SRCREV_machine_pn-linux-yocto_crownbay ?= "19f7e43b54aef08d58135ed2a897d77b624b320a"
SRCREV_meta_pn-linux-yocto_crownbay ?= "d7a96809a585e06933d8c08adb9b9f66b21efb4c"
SRCREV_emgd_pn-linux-yocto_crownbay ?= "86643bdd8cbad616a161ab91f51108cf0da827bc"

SRCREV_machine_pn-linux-yocto_crownbay-noemgd ?= "19f7e43b54aef08d58135ed2a897d77b624b320a"
SRCREV_meta_pn-linux-yocto_crownbay-noemgd ?= "d7a96809a585e06933d8c08adb9b9f66b21efb4c"

KSRC_linux_yocto_3_4 ?= "git.yoctoproject.org/linux-yocto-3.4.git"
SRC_URI_crownbay = "git://git.yoctoproject.org/linux-yocto-3.4.git;protocol=git;nocheckout=1;branch=${KBRANCH},meta,emgd-1.14;name=machine,meta,emgd"
SRC_URI_crownbay-noemgd = "git://git.yoctoproject.org/linux-yocto-3.4.git;protocol=git;nocheckout=1;branch=${KBRANCH},meta;name=machine,meta"
