FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2 = "fri2"
#KBRANCH_fri2 = "standard/preempt-rt/fri2"
SRCREV_machine_pn-linux-yocto-rt_fri2 ?= "4ed758e1861621b6db687498e88991b5034cfa78"
#SRCREV_meta_pn-linux-yocto-rt_fri2 ?= #"c5bddf8ea379406ffec550528e17b777a0eba24b"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
#KBRANCH_fri2-noemgd = "standard/preempt-rt/fri2"
SRCREV_machine_pn-linux-yocto-rt_fri2-noemgd ?= "4ed758e1861621b6db687498e88991b5034cfa78"
#SRCREV_meta_pn-linux-yocto-rt_fri2-noemgd ?= "c5bddf8ea379406ffec550528e17b777a0eba24b"

module_autoload_iwlwifi = "iwlwifi"
