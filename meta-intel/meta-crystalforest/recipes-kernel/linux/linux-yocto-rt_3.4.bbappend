FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crystalforest-stargo = "crystalforest-stargo"
KMACHINE_crystalforest-stargo  = "crystalforest"
KBRANCH_crystalforest-stargo = "standard/preempt-rt/base"

SRCREV_machine_pn-linux-yocto-rt_crystalforest-stargo ?= "9032b1e9daf5b4396f939981c3be95f67802d18c"
SRCREV_meta_pn-linux-yocto-rt_crystalforest-stargo ?= "9e3bdb7344054264b750e53fbbb6394cc1c942ac"


COMPATIBLE_MACHINE_crystalforest-shumway = "crystalforest-shumway"
KMACHINE_crystalforest-shumway  = "crystalforest"
KBRANCH_crystalforest-shumway = "standard/preempt-rt/base"

SRCREV_machine_pn-linux-yocto-rt_crystalforest-shumway ?= "9032b1e9daf5b4396f939981c3be95f67802d18c"
SRCREV_meta_pn-linux-yocto-rt_crystalforest-shumway ?= "9e3bdb7344054264b750e53fbbb6394cc1c942ac"

module_autoload_uio = "uio"
