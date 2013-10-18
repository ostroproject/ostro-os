FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crystalforest-gladden = "crystalforest-gladden"
KMACHINE_crystalforest-gladden  = "crystalforest"
KBRANCH_crystalforest-gladden  = "standard/common-pc-64/crystalforest"

SRCREV_machine_pn-linux-yocto_crystalforest-gladden ?= "dbf932a9b316d5b29b3e220e5a30e7a165ad2992"
SRCREV_meta_pn-linux-yocto_crystalforest-gladden ?= "cb96851e7e559f9247d616d08406db6135c357cb"

COMPATIBLE_MACHINE_crystalforest-server = "crystalforest-server"
KMACHINE_crystalforest-server  = "crystalforest"
KBRANCH_crystalforest-server  = "standard/common-pc-64/crystalforest"

SRCREV_machine_pn-linux-yocto_crystalforest-server ?= "dbf932a9b316d5b29b3e220e5a30e7a165ad2992"
SRCREV_meta_pn-linux-yocto_crystalforest-server ?= "cb96851e7e559f9247d616d08406db6135c357cb"

LINUX_VERSION = "3.8.13"

module_autoload_uio = "uio"
