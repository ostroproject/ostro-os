FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_emenlow = "emenlow"
KMACHINE_emenlow  = "yocto/standard/emenlow"
KERNEL_FEATURES_append_emenlow += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto_emenlow ?= "629e2581c88e7db9c4a844ddbf9c7a4087de18a0"
SRCREV_meta_pn-linux-yocto_emenlow ?= "ae3e64c077972fe87f09946bd215620df68ca327"
