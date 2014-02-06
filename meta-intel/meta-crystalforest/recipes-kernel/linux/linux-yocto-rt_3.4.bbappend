FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"


COMPATIBLE_MACHINE_crystalforest-gladden = "crystalforest-gladen"
KMACHINE_crystalforest-gladden  = "crystalforest"
KBRANCH_crystalforest-gladden = "standard/preempt-rt/base"

SRCREV_machine_pn-linux-yocto-rt_crystalforest-gladden ?= "3d56b103cd7072d520c395194e620aba2f6e52e3"
SRCREV_meta_pn-linux-yocto-rt_crystalforest-gladden ?= "f697e099bc76d5df3a307a5bc0cc25021dd6dfe0"

COMPATIBLE_MACHINE_crystalforest-server = "crystalforest-server"
KMACHINE_crystalforest-server  = "crystalforest"
KBRANCH_crystalforest-server = "standard/preempt-rt/base"

SRCREV_machine_pn-linux-yocto-rt_crystalforest-server ?= "3d56b103cd7072d520c395194e620aba2f6e52e3"
SRCREV_meta_pn-linux-yocto-rt_crystalforest-server ?= "f697e099bc76d5df3a307a5bc0cc25021dd6dfe0"

module_autoload_uio = "uio"

LINUX_VERSION = "3.4.28"
