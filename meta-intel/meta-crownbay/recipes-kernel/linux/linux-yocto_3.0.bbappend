FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay  = "yocto/standard/crownbay"
KERNEL_FEATURES_append_crownbay += " cfg/smp.scc"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd  = "yocto/standard/crownbay"
KERNEL_FEATURES_append_crownbay-noemgd += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto_crownbay ?= "6b4b9acde5fb0ff66ae58fa98274bfe631501499"
SRCREV_meta_pn-linux-yocto_crownbay ?= "5b535279e61197cb194bb2dfceb8b7a04128387c"

SRCREV_machine_pn-linux-yocto_crownbay-noemgd ?= "6b4b9acde5fb0ff66ae58fa98274bfe631501499"
SRCREV_meta_pn-linux-yocto_crownbay-noemgd ?= "5b535279e61197cb194bb2dfceb8b7a04128387c"
