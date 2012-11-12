FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crystalforest-gladden = "crystalforest-gladen"
KMACHINE_crystalforest-gladden  = "crystalforest"
KBRANCH_crystalforest-gladden = "standard/preempt-rt/base"

SRCREV_machine_pn-linux-yocto-rt_crystalforest-gladden ?= "${AUTOREV}"
SRCREV_meta_pn-linux-yocto-rt_crystalforest-gladden ?= "${AUTOREV}"

COMPATIBLE_MACHINE_crystalforest-server = "crystalforest-server"
KMACHINE_crystalforest-server  = "crystalforest"
KBRANCH_crystalforest-server = "standard/preempt-rt/base"

SRCREV_machine_pn-linux-yocto-rt_crystalforest-server ?= "${AUTOREV}"
SRCREV_meta_pn-linux-yocto-rt_crystalforest-server ?= "${AUTOREV}"

module_autoload_uio = "uio"
