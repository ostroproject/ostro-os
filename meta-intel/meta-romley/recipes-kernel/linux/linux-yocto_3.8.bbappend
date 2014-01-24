FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

PACKAGE_ARCH_romley = "${MACHINE_ARCH}"
PACKAGE_ARCH_romley-ivb = "${MACHINE_ARCH}"

COMPATIBLE_MACHINE_romley = "romley"

KMACHINE_romley  = "romley"
KBRANCH_romley  = "standard/common-pc-64/romley"

SRCREV_machine_pn-linux-yocto_romley ?= "dbf932a9b316d5b29b3e220e5a30e7a165ad2992"
SRCREV_meta_pn-linux-yocto_romley ?= "cb96851e7e559f9247d616d08406db6135c357cb"

COMPATIBLE_MACHINE_romley-ivb = "romley-ivb"
KMACHINE_romley-ivb  = "romley"
KBRANCH_romley-ivb  = "standard/common-pc-64/romley"

SRCREV_machine_pn-linux-yocto_romley-ivb ?= "dbf932a9b316d5b29b3e220e5a30e7a165ad2992"
SRCREV_meta_pn-linux-yocto_romley-ivb ?= "cb96851e7e559f9247d616d08406db6135c357cb"

LINUX_VERSION = "3.8.13"

module_autoload_uio = "uio"
