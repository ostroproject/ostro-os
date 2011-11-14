FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fishriver = "fishriver"
KMACHINE_fishriver  = "yocto/standard/fishriver"
KERNEL_FEATURES_append_fishriver += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto_fishriver ?= "947ec2b64f6920ab67f2afbfc074da2b222d9b67"
SRCREV_meta_pn-linux-yocto_fishriver ?= "ae3e64c077972fe87f09946bd215620df68ca327"
