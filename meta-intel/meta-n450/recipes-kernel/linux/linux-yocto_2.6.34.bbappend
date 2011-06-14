FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"
KMACHINE_n450 = "atom-pc"
COMPATIBLE_MACHINE_n450 = "n450"

# The n450 is a single core hypterthreaded CPU
KERNEL_FEATURES_append_n450 += " cfg/smp.scc"

# We use the atom-pc machine SRCREV and the default meta SRCREV
#SRCREV_machine_pn-linux-yocto-stable_n450 = ""
#SRCREV_meta_pn-linux-yocto-stable_n450 ?= ""
