FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crystalforest-gladden = "crystalforest-gladden"
KMACHINE_crystalforest-gladden  = "crystalforest"
KBRANCH_crystalforest-gladden  = "standard/common-pc-64/crystalforest"

SRCREV_machine_pn-linux-yocto_crystalforest-gladden ?= "47aed0c17c1c55988198ad39f86ae88894c8e0a4"
SRCREV_meta_pn-linux-yocto_crystalforest-gladden ?= "2a6d36e75ca0a121570a389d7bab76ec240cbfda"

COMPATIBLE_MACHINE_crystalforest-server = "crystalforest-server"
KMACHINE_crystalforest-server  = "crystalforest"
KBRANCH_crystalforest-server  = "standard/common-pc-64/crystalforest"

SRCREV_machine_pn-linux-yocto_crystalforest-server ?= "47aed0c17c1c55988198ad39f86ae88894c8e0a4"
SRCREV_meta_pn-linux-yocto_crystalforest-server ?= "2a6d36e75ca0a121570a389d7bab76ec240cbfda"

LINUX_VERSION = "3.8.4"

module_autoload_uio = "uio"
