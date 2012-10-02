FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay  = "crownbay"
KBRANCH_crownbay  = "standard/crownbay"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd  = "crownbay"
KBRANCH_crownbay-noemgd  = "standard/crownbay"

SRCREV_machine_pn-linux-yocto_crownbay ?= "3fa06aa29078fdb2af431de2d3fdae7d281ba85f"
SRCREV_meta_pn-linux-yocto_crownbay ?= "5bdc655034a58a7147176a8a882d81e2fd51e4b9"
SRCREV_emgd_pn-linux-yocto_crownbay ?= "86643bdd8cbad616a161ab91f51108cf0da827bc"

SRCREV_machine_pn-linux-yocto_crownbay-noemgd ?= "3fa06aa29078fdb2af431de2d3fdae7d281ba85f"
SRCREV_meta_pn-linux-yocto_crownbay-noemgd ?= "5bdc655034a58a7147176a8a882d81e2fd51e4b9"

KSRC_linux_yocto_3_4 ?= "git.yoctoproject.org/linux-yocto-3.4.git"
SRC_URI_crownbay = "git://git.yoctoproject.org/linux-yocto-3.4.git;protocol=git;nocheckout=1;branch=${KBRANCH},meta,emgd-1.14;name=machine,meta,emgd"
SRC_URI_crownbay-noemgd = "git://git.yoctoproject.org/linux-yocto-3.4.git;protocol=git;nocheckout=1;branch=${KBRANCH},meta;name=machine,meta"
