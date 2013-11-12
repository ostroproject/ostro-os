FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_romley = "romley"

KMACHINE_romley  = "romley"
KBRANCH_romley  = "standard/common-pc-64/romley"

SRCREV_machine_pn-linux-yocto_romley ?= "c03195ed6e3066494e3fb4be69154a57066e845b"
SRCREV_meta_pn-linux-yocto_romley ?= "f1c9080cd27f99700fa59b5375d1ddd0afe625ad"

COMPATIBLE_MACHINE_romley-ivb = "romley-ivb"
KMACHINE_romley-ivb  = "romley"
KBRANCH_romley-ivb  = "standard/common-pc-64/romley"

SRCREV_machine_pn-linux-yocto_romley-ivb ?= "c03195ed6e3066494e3fb4be69154a57066e845b"
SRCREV_meta_pn-linux-yocto_romley-ivb ?= "f1c9080cd27f99700fa59b5375d1ddd0afe625ad"

LINUX_VERSION = "3.10.17"

module_autoload_uio = "uio"
