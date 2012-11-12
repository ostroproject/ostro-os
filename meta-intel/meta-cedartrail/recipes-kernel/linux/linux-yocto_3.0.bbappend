FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

SRC_URI_cedartrail = "git://git.yoctoproject.org/linux-yocto-3.0;protocol=git;bareclone=1;branch=${KBRANCH},meta,yocto/pvr;name=machine,meta,pvr"

SRC_URI_cedartrail-nopvr = "git://git.yoctoproject.org/linux-yocto-3.0;protocol=git;nocheckout=1;branch=${KBRANCH},meta;name=machine,meta"

COMPATIBLE_MACHINE_cedartrail = "cedartrail"
KMACHINE_cedartrail  = "cedartrail"
KBRANCH_cedartrail  = "yocto/standard/cedartrail"
KERNEL_FEATURES_append_cedartrail += "bsp/cedartrail/cedartrail-pvr-merge.scc"
KERNEL_FEATURES_append_cedartrail += "cfg/efi-ext.scc"

COMPATIBLE_MACHINE_cedartrail-nopvr = "cedartrail"
KMACHINE_cedartrail-nopvr  = "cedartrail"
KBRANCH_cedartrail-nopvr  = "yocto/standard/cedartrail"
KERNEL_FEATURES_append_cedartrail-nopvr += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto_cedartrail ?= "${AUTOREV}"
SRCREV_meta_pn-linux-yocto_cedartrail ?= "${AUTOREV}"
SRCREV_pvr_pn-linux-yocto_cedartrail ?= "${AUTOREV}"

SRCREV_machine_pn-linux-yocto_cedartrail-nopvr ?= "${AUTOREV}"
SRCREV_meta_pn-linux-yocto_cedartrail-nopvr ?= "${AUTOREV}"
