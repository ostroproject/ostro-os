FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crystalforest-gladden = "crystalforest-gladden"
KMACHINE_crystalforest-gladden  = "crystalforest"
KBRANCH_crystalforest-gladden  = "standard/common-pc-64/crystalforest"

SRCREV_machine_pn-linux-yocto_crystalforest-gladden ?= "85cdabba08d484bdcc4b25f0bbc23ac60c75aa5b"
SRCREV_meta_pn-linux-yocto_crystalforest-gladden ?= "452f0679ea93a6cb4433bebd7177629228a5cf68"

COMPATIBLE_MACHINE_crystalforest-server = "crystalforest-server"
KMACHINE_crystalforest-server  = "crystalforest"
KBRANCH_crystalforest-server  = "standard/common-pc-64/crystalforest"

SRCREV_machine_pn-linux-yocto_crystalforest-server ?= "85cdabba08d484bdcc4b25f0bbc23ac60c75aa5b"
SRCREV_meta_pn-linux-yocto_crystalforest-server ?= "452f0679ea93a6cb4433bebd7177629228a5cf68"

LINUX_VERSION = "3.10.11"

module_autoload_uio = "uio"
