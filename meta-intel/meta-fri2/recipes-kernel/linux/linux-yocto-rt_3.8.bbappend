FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

PACKAGE_ARCH_fri2 = "${MACHINE_ARCH}"
PACKAGE_ARCH_fri2-noemgd = "${MACHINE_ARCH}"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2 = "fri2"
KBRANCH_fri2 = "standard/preempt-rt/fri2"
SRCREV_machine_pn-linux-yocto-rt_fri2 ?= "220f0ff77dbc46b06ec66c1e50afc4b9eb563c97"
#SRCREV_meta_pn-linux-yocto-rt_fri2 ?= "XXX"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
KBRANCH_fri2-noemgd = "standard/preempt-rt/fri2"
SRCREV_machine_pn-linux-yocto-rt_fri2-noemgd ?= "220f0ff77dbc46b06ec66c1e50afc4b9eb563c97"
#SRCREV_meta_pn-linux-yocto-rt_fri2-noemgd ?= "XXX"

module_autoload_iwlwifi = "iwlwifi"
