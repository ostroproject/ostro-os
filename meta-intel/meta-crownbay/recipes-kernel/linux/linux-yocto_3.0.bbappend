FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay  = "yocto/standard/crownbay"
KERNEL_FEATURES_append_crownbay += " cfg/smp.scc"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd  = "yocto/standard/crownbay"
KERNEL_FEATURES_append_crownbay-noemgd += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto_crownbay ?= "63c65842a3a74e4bd3128004ac29b5639f16433f"
SRCREV_meta_pn-linux-yocto_crownbay ?= "59314a3523e360796419d76d78c6f7d8c5ef2593"

SRCREV_machine_pn-linux-yocto_crownbay-noemgd ?= "63c65842a3a74e4bd3128004ac29b5639f16433f"
SRCREV_meta_pn-linux-yocto_crownbay-noemgd ?= "59314a3523e360796419d76d78c6f7d8c5ef2593"
