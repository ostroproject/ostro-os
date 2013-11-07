FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crystalforest-gladden = "crystalforest-gladden"
KMACHINE_crystalforest-gladden  = "crystalforest"
KBRANCH_crystalforest-gladden  = "standard/common-pc-64/crystalforest"

SRCREV_machine_pn-linux-yocto_crystalforest-gladden ?= "85cdabba08d484bdcc4b25f0bbc23ac60c75aa5b"
SRCREV_meta_pn-linux-yocto_crystalforest-gladden ?= "f1c9080cd27f99700fa59b5375d1ddd0afe625ad"

COMPATIBLE_MACHINE_crystalforest-server = "crystalforest-server"
KMACHINE_crystalforest-server  = "crystalforest"
KBRANCH_crystalforest-server  = "standard/common-pc-64/crystalforest"

SRCREV_machine_pn-linux-yocto_crystalforest-server ?= "85cdabba08d484bdcc4b25f0bbc23ac60c75aa5b"
SRCREV_meta_pn-linux-yocto_crystalforest-server ?= "f1c9080cd27f99700fa59b5375d1ddd0afe625ad"

LINUX_VERSION = "3.10.11"

module_autoload_uio = "uio"
