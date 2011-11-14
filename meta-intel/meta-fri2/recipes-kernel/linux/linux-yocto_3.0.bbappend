FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2  = "yocto/standard/fri2"
KERNEL_FEATURES_append_fri2 += " cfg/smp.scc"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd  = "yocto/standard/fri2"
KERNEL_FEATURES_append_fri2-noemgd += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto_fri2 ?= "bdb0cabe7bd20b74c47d6d4e65d14c633028bfea"
SRCREV_meta_pn-linux-yocto_fri2 ?= "ae3e64c077972fe87f09946bd215620df68ca327"

SRCREV_machine_pn-linux-yocto_fri2-noemgd ?= "bdb0cabe7bd20b74c47d6d4e65d14c633028bfea"
SRCREV_meta_pn-linux-yocto_fri2-noemgd ?= "ae3e64c077972fe87f09946bd215620df68ca327"
