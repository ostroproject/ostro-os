FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_cedartrail = "cedartrail"
KMACHINE_cedartrail  = "yocto/standard/cedartrail"
KERNEL_FEATURES_append_cedartrail += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto_cedartrail ?= "f389d310965a56091f688b28ea8be6d9cbb7fbbe"
SRCREV_meta_pn-linux-yocto_cedartrail ?= "04a52a32cbdf0972033b97b83eaa83eb275dfdc9"
