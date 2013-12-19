FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_romley = "romley"

KMACHINE_romley  = "romley"
KBRANCH_romley  = "standard/common-pc-64/romley"

SRCREV_machine_pn-linux-yocto_romley ?= "c03195ed6e3066494e3fb4be69154a57066e845b"
SRCREV_meta_pn-linux-yocto_romley ?= "f1c9080cd27f99700fa59b5375d1ddd0afe625ad"

COMPATIBLE_MACHINE_romley-ivb = "romley-ivb"
KMACHINE_romley-ivb  = "romley"
KBRANCH_romley-ivb  = "standard/common-pc-64/romley"

SRCREV_machine_pn-linux-yocto_romley-ivb ?= "a9ec82e355130160f9094e670bd5be0022a84194"
SRCREV_meta_pn-linux-yocto_romley-ivb ?= "d9cd83c0292bd4e2a6754a96761027252e726a42"

LINUX_VERSION = "3.10.19"

module_autoload_uio = "uio"
