FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_fri2 = "fri2"
KMACHINE_fri2 = "fri2"
#KBRANCH_fri2 = "standard/preempt-rt/fri2"
SRCREV_machine_pn-linux-yocto-rt_fri2 ?= "5a748ac8780f72a115c9d6eabe4043e208e7f54f"
SRCREV_meta_pn-linux-yocto-rt_fri2 ?= "e7f2fdc48f8808887175f0328274a2668084738c"

COMPATIBLE_MACHINE_fri2-noemgd = "fri2-noemgd"
KMACHINE_fri2-noemgd = "fri2"
#KBRANCH_fri2-noemgd = "standard/preempt-rt/fri2"
SRCREV_machine_pn-linux-yocto-rt_fri2-noemgd ?= "5a748ac8780f72a115c9d6eabe4043e208e7f54f"
SRCREV_meta_pn-linux-yocto-rt_fri2-noemgd ?= "e7f2fdc48f8808887175f0328274a2668084738c"

module_autoload_iwlwifi = "iwlwifi"

LINUX_VERSION = "3.2.32"
