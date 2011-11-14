FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay  = "yocto/standard/crownbay"
KERNEL_FEATURES_append_crownbay += " cfg/smp.scc"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd  = "yocto/standard/crownbay"
KERNEL_FEATURES_append_crownbay-noemgd += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto_crownbay ?= "94e7946b9e121bc32812d33b4a064480a52f5938"
SRCREV_meta_pn-linux-yocto_crownbay ?= "ae3e64c077972fe87f09946bd215620df68ca327"

SRCREV_machine_pn-linux-yocto_crownbay-noemgd ?= "94e7946b9e121bc32812d33b4a064480a52f5938"
SRCREV_meta_pn-linux-yocto_crownbay-noemgd ?= "ae3e64c077972fe87f09946bd215620df68ca327"
