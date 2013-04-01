FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_romley = "romley"

KMACHINE_romley  = "romley"
KBRANCH_romley  = "standard/common-pc-64/romley"

SRCREV_machine_pn-linux-yocto_romley ?= "47aed0c17c1c55988198ad39f86ae88894c8e0a4"
SRCREV_meta_pn-linux-yocto_romley ?= "2a6d36e75ca0a121570a389d7bab76ec240cbfda"

COMPATIBLE_MACHINE_romley-ivb = "romley-ivb"
KMACHINE_romley-ivb  = "romley"
KBRANCH_romley-ivb  = "standard/common-pc-64/romley"

SRCREV_machine_pn-linux-yocto_romley-ivb ?= "47aed0c17c1c55988198ad39f86ae88894c8e0a4"
SRCREV_meta_pn-linux-yocto_romley-ivb ?= "2a6d36e75ca0a121570a389d7bab76ec240cbfda"

LINUX_VERSION = "3.8.4"

module_autoload_uio = "uio"
