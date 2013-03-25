FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_romley = "romley"

KMACHINE_romley  = "romley"
KBRANCH_romley  = "standard/common-pc-64/romley"

SRCREV_machine_pn-linux-yocto_romley ?= "b170394a475b96ecc92cbc9e4b002bed0a9f69c5"
SRCREV_meta_pn-linux-yocto_romley ?= "c2ed0f16fdec628242a682897d5d86df4547cf24"

COMPATIBLE_MACHINE_romley-ivb = "romley-ivb"
KMACHINE_romley-ivb  = "romley"
KBRANCH_romley-ivb  = "standard/common-pc-64/romley"

SRCREV_machine_pn-linux-yocto_romley-ivb ?= "b170394a475b96ecc92cbc9e4b002bed0a9f69c5"
SRCREV_meta_pn-linux-yocto_romley-ivb ?= "c2ed0f16fdec628242a682897d5d86df4547cf24"

module_autoload_uio = "uio"
