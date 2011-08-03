FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay  = "yocto/standard/crownbay"
KERNEL_FEATURES_append_crownbay += " cfg/smp.scc"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd  = "yocto/standard/crownbay"
KERNEL_FEATURES_append_crownbay-noemgd += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto_crownbay ?= "9a259cf4f6d404db2820642df755a295bbfb7fe7"
SRCREV_meta_pn-linux-yocto_crownbay ?= "fe8eac15e144a35a716cd32c9d2b296ecd5202ac"

SRCREV_machine_pn-linux-yocto_crownbay-noemgd ?= "9a259cf4f6d404db2820642df755a295bbfb7fe7"
SRCREV_meta_pn-linux-yocto_crownbay-noemgd ?= "fe8eac15e144a35a716cd32c9d2b296ecd5202ac"
