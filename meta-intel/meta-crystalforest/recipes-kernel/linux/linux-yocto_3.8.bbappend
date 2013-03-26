FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crystalforest-gladden = "crystalforest-gladden"
KMACHINE_crystalforest-gladden  = "crystalforest"
KBRANCH_crystalforest-gladden  = "standard/common-pc-64/crystalforest"

SRCREV_machine_pn-linux-yocto_crystalforest-gladden ?= "b170394a475b96ecc92cbc9e4b002bed0a9f69c5"
SRCREV_meta_pn-linux-yocto_crystalforest-gladden ?= "c2ed0f16fdec628242a682897d5d86df4547cf24"

COMPATIBLE_MACHINE_crystalforest-server = "crystalforest-server"
KMACHINE_crystalforest-server  = "crystalforest"
KBRANCH_crystalforest-server  = "standard/common-pc-64/crystalforest"

SRCREV_machine_pn-linux-yocto_crystalforest-server ?= "b170394a475b96ecc92cbc9e4b002bed0a9f69c5"
SRCREV_meta_pn-linux-yocto_crystalforest-server ?= "c2ed0f16fdec628242a682897d5d86df4547cf24"

module_autoload_uio = "uio"
