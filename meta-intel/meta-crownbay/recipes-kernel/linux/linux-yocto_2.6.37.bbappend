FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay  = "yocto/standard/crownbay"
KERNEL_FEATURES_append_crownbay += " cfg/smp.scc"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd  = "yocto/standard/crownbay"
KERNEL_FEATURES_append_crownbay-noemgd += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto_crownbay ?= "88ea187941f262518b3b8194e042f0270fdf27c4"
SRCREV_meta_pn-linux-yocto_crownbay ?= "f1dc3722d45cdcc92c84ebfecf4ce616d2efed26"

SRCREV_machine_pn-linux-yocto_crownbay-noemgd ?= "88ea187941f262518b3b8194e042f0270fdf27c4"
SRCREV_meta_pn-linux-yocto_crownbay-noemgd ?= "f1dc3722d45cdcc92c84ebfecf4ce616d2efed26"
