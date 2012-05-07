FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2 = "fri2"
#KBRANCH_fri2 = "standard/preempt-rt/base"
SRCREV_machine_pn-linux-yocto_fri2 ?= "44e0381c0e0d46d3b9f171a58cb0ec5c2077b176"
SRCREV_meta_pn-linux-yocto_fri2 ?= "6b3d4e09aa2531e9649f3f03827b7efbccfcec03"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
#KBRANCH_fri2-noemgd = "standard/preempt-rt/base"
SRCREV_machine_pn-linux-yocto_fri2-noemgd ?= "44e0381c0e0d46d3b9f171a58cb0ec5c2077b176"
SRCREV_meta_pn-linux-yocto_fri2-noemgd ?= "6b3d4e09aa2531e9649f3f03827b7efbccfcec03"

module_autoload_iwlwifi = "iwlwifi"
