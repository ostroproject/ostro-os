FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay  = "yocto/standard/crownbay"
KERNEL_FEATURES_append_crownbay += " cfg/smp.scc"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd  = "yocto/standard/crownbay"
KERNEL_FEATURES_append_crownbay-noemgd += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto_crownbay ?= "372c0ab135978bd8ca3a77c88816a25c5ed8f303"
SRCREV_meta_pn-linux-yocto_crownbay ?= "d5d3c6480d61f83503ccef7fbcd765f7aca8b71b"

SRCREV_machine_pn-linux-yocto_crownbay-noemgd ?= "372c0ab135978bd8ca3a77c88816a25c5ed8f303"
SRCREV_meta_pn-linux-yocto_crownbay-noemgd ?= "d5d3c6480d61f83503ccef7fbcd765f7aca8b71b"
