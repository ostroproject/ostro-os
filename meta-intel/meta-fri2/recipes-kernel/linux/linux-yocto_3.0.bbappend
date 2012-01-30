FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2  = "yocto/standard/fri2"
KERNEL_FEATURES_append_fri2 += " cfg/smp.scc cfg/efi-ext.scc"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd  = "yocto/standard/fri2"
KERNEL_FEATURES_append_fri2-noemgd += " cfg/smp.scc cfg/efi-ext.scc"

SRCREV_machine_pn-linux-yocto_fri2 ?= "16a35563a2a5cb3debc9d0666cbdc3b8d5d43b74"
SRCREV_meta_pn-linux-yocto_fri2 ?= "59314a3523e360796419d76d78c6f7d8c5ef2593"

SRCREV_machine_pn-linux-yocto_fri2-noemgd ?= "16a35563a2a5cb3debc9d0666cbdc3b8d5d43b74"
SRCREV_meta_pn-linux-yocto_fri2-noemgd ?= "59314a3523e360796419d76d78c6f7d8c5ef2593"
