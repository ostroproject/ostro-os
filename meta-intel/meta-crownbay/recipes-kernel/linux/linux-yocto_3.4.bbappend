FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay  = "crownbay"
KBRANCH_crownbay  = "standard/crownbay"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd  = "crownbay"
KBRANCH_crownbay-noemgd  = "standard/crownbay"

SRCREV_machine_pn-linux-yocto_crownbay ?= "${AUTOREV}"
SRCREV_meta_pn-linux-yocto_crownbay ?= "${AUTOREV}"
SRCREV_emgd_pn-linux-yocto_crownbay ?= "${AUTOREV}"

SRCREV_machine_pn-linux-yocto_crownbay-noemgd ?= "${AUTOREV}"
SRCREV_meta_pn-linux-yocto_crownbay-noemgd ?= "${AUTOREV}"

KSRC_linux_yocto_3_4 ?= "git.yoctoproject.org/linux-yocto-3.4.git"
SRC_URI_crownbay = "git://git.yoctoproject.org/linux-yocto-3.4.git;protocol=git;nocheckout=1;branch=${KBRANCH},meta,emgd-1.14;name=machine,meta,emgd"
SRC_URI_crownbay-noemgd = "git://git.yoctoproject.org/linux-yocto-3.4.git;protocol=git;nocheckout=1;branch=${KBRANCH},meta;name=machine,meta"
