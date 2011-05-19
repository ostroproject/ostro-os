FILESEXTRAPATHS := "${FILESEXTRAPATHS}:${THISDIR}/${PN}"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay  = "crownbay"
KERNEL_FEATURES_append_crownbay += " cfg/smp.scc"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd  = "crownbay"
KERNEL_FEATURES_append_crownbay-noemgd += " cfg/smp.scc"
