FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2  = "yocto/standard/fri2"
KERNEL_FEATURES_append_fri2 += " cfg/smp.scc cfg/efi-ext.scc"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd  = "yocto/standard/fri2"
KERNEL_FEATURES_append_fri2-noemgd += " cfg/smp.scc cfg/efi-ext.scc"

SRCREV_machine_pn-linux-yocto_fri2 ?= "7c20bf8e1ef00f00f91c330c887d2b9c06c82d48"
SRCREV_meta_pn-linux-yocto_fri2 ?= "caa74f86f42f6ecc22c3e9f380176b2695579e18"

SRCREV_machine_pn-linux-yocto_fri2-noemgd ?= "7c20bf8e1ef00f00f91c330c887d2b9c06c82d48"
SRCREV_meta_pn-linux-yocto_fri2-noemgd ?= "caa74f86f42f6ecc22c3e9f380176b2695579e18"
