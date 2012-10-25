FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crystalforest-stargo = "crystalforest-stargo"
KMACHINE_crystalforest-stargo  = "crystalforest"
KBRANCH_crystalforest-stargo  = "standard/common-pc-64/crystalforest"

SRCREV_machine_pn-linux-yocto_crystalforest-stargo ?= "449f7f520350700858f21a5554b81cc8ad23267d"
SRCREV_meta_pn-linux-yocto_crystalforest-stargo ?= "2ec32d511b62d44b63e8560a9b1d6895a5dac695"

COMPATIBLE_MACHINE_crystalforest-shumway = "crystalforest-shumway"
KMACHINE_crystalforest-shumway  = "crystalforest"
KBRANCH_crystalforest-shumway  = "standard/common-pc-64/crystalforest"

SRCREV_machine_pn-linux-yocto_crystalforest-shumway ?= "449f7f520350700858f21a5554b81cc8ad23267d"
SRCREV_meta_pn-linux-yocto_crystalforest-shumway ?= "2ec32d511b62d44b63e8560a9b1d6895a5dac695"

module_autoload_uio = "uio"
