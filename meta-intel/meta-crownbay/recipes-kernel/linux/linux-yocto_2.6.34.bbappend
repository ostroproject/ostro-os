FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay  = "crownbay"
KERNEL_FEATURES_append_crownbay += " cfg/smp.scc"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd  = "crownbay"
KERNEL_FEATURES_append_crownbay-noemgd += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto_crownbay ?= "56fe215d3f1a2cc3a5a26482ac9809ba44495695"
SRCREV_meta_pn-linux-yocto_crownbay ?= "ec26387cb168e9e0976999b528b5a9dd62e3157a"

RCREV_machine_pn-linux-yocto_crownbay-noemgd ?= "56fe215d3f1a2cc3a5a26482ac9809ba44495695"
SRCREV_meta_pn-linux-yocto_crownbay-noemgd ?= "ec26387cb168e9e0976999b528b5a9dd62e3157a"
