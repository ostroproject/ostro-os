FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"
COMPATIBLE_MACHINE_n450 = "n450"
KMACHINE_n450  = "yocto/standard/common-pc/atom-pc"

# The n450 is a single core hypterthreaded CPU
KERNEL_FEATURES_append_n450 += " cfg/smp.scc"

SRCREV_machine_pn-linux-yocto_n450 = "c54453332efbd86c2ea3caa64e908b39cfac1e76"
#SRCREV_meta_pn-linux-yocto_n450 ?= XXXX
