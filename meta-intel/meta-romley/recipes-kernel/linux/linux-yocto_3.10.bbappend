FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_romley = "romley"

KMACHINE_romley  = "romley"
KBRANCH_romley  = "standard/common-pc-64/romley"

SRCREV_machine_pn-linux-yocto_romley ?= "85cdabba08d484bdcc4b25f0bbc23ac60c75aa5b"
SRCREV_meta_pn-linux-yocto_romley ?= "452f0679ea93a6cb4433bebd7177629228a5cf68"

COMPATIBLE_MACHINE_romley-ivb = "romley-ivb"
KMACHINE_romley-ivb  = "romley"
KBRANCH_romley-ivb  = "standard/common-pc-64/romley"

SRCREV_machine_pn-linux-yocto_romley-ivb ?= "85cdabba08d484bdcc4b25f0bbc23ac60c75aa5b"
SRCREV_meta_pn-linux-yocto_romley-ivb ?= "452f0679ea93a6cb4433bebd7177629228a5cf68"

LINUX_VERSION = "3.10.11"

module_autoload_uio = "uio"
