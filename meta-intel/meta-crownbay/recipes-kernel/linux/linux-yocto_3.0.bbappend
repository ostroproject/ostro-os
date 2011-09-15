FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay  = "yocto/standard/crownbay"
KERNEL_FEATURES_append_crownbay += " cfg/smp.scc"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd  = "yocto/standard/crownbay"
KERNEL_FEATURES_append_crownbay-noemgd += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto_crownbay ?= "2247da9131ea7e46ed4766a69bb1353dba22f873"
SRCREV_meta_pn-linux-yocto_crownbay ?= "12574e5a77597f6938315ef82d18fc5e229fb79c"

SRCREV_machine_pn-linux-yocto_crownbay-noemgd ?= "2247da9131ea7e46ed4766a69bb1353dba22f873"
SRCREV_meta_pn-linux-yocto_crownbay-noemgd ?= "12574e5a77597f6938315ef82d18fc5e229fb79c"
