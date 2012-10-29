FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay  = "crownbay"
KBRANCH_crownbay  = "standard/crownbay"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd  = "crownbay"
KBRANCH_crownbay-noemgd  = "standard/crownbay"

SRCREV_machine_pn-linux-yocto_crownbay ?= "218bd8d2022b9852c60d32f0d770931e3cf343e2"
SRCREV_meta_pn-linux-yocto_crownbay ?= "68a635bf8dfb64b02263c1ac80c948647cc76d5f"
SRCREV_emgd_pn-linux-yocto_crownbay ?= "86643bdd8cbad616a161ab91f51108cf0da827bc"

SRCREV_machine_pn-linux-yocto_crownbay-noemgd ?= "218bd8d2022b9852c60d32f0d770931e3cf343e2"
SRCREV_meta_pn-linux-yocto_crownbay-noemgd ?= "68a635bf8dfb64b02263c1ac80c948647cc76d5f"

KSRC_linux_yocto_3_4 ?= "git.yoctoproject.org/linux-yocto-3.4.git"
SRC_URI_crownbay = "git://git.yoctoproject.org/linux-yocto-3.4.git;protocol=git;nocheckout=1;branch=${KBRANCH},meta,emgd-1.14;name=machine,meta,emgd"
SRC_URI_crownbay-noemgd = "git://git.yoctoproject.org/linux-yocto-3.4.git;protocol=git;nocheckout=1;branch=${KBRANCH},meta;name=machine,meta"

LINUX_VERSION = "3.4.11"
