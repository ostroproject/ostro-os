FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crystalforest-gladden = "crystalforest-gladen"
KMACHINE_crystalforest-gladden  = "crystalforest"
KBRANCH_crystalforest-gladden = "standard/preempt-rt/base"

SRCREV_machine_pn-linux-yocto-rt_crystalforest-gladden ?= "9032b1e9daf5b4396f939981c3be95f67802d18c"
SRCREV_meta_pn-linux-yocto-rt_crystalforest-gladden ?= "9e3bdb7344054264b750e53fbbb6394cc1c942ac"

COMPATIBLE_MACHINE_crystalforest-server = "crystalforest-server"
KMACHINE_crystalforest-server  = "crystalforest"
KBRANCH_crystalforest-server = "standard/preempt-rt/base"

SRCREV_machine_pn-linux-yocto-rt_crystalforest-server ?= "9032b1e9daf5b4396f939981c3be95f67802d18c"
SRCREV_meta_pn-linux-yocto-rt_crystalforest-server ?= "9e3bdb7344054264b750e53fbbb6394cc1c942ac"

module_autoload_uio = "uio"
