FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crystalforest-stargo = "crystalforest-stargo"
KMACHINE_crystalforest-stargo  = "crystalforest"
KBRANCH_crystalforest-stargo = "standard/preempt-rt/base"

SRCREV_machine_pn-linux-yocto-rt_crystalforest-stargo ?= "9032b1e9daf5b4396f939981c3be95f67802d18c"
SRCREV_meta_pn-linux-yocto-rt_crystalforest-stargo ?= "463299bc2e533e1bd38b0053ae7b210980f269c3"


COMPATIBLE_MACHINE_crystalforest-shumway = "crystalforest-shumway"
KMACHINE_crystalforest-shumway  = "crystalforest"
KBRANCH_crystalforest-shumway = "standard/preempt-rt/base"

SRCREV_machine_pn-linux-yocto-rt_crystalforest-shumway ?= "9032b1e9daf5b4396f939981c3be95f67802d18c"
SRCREV_meta_pn-linux-yocto-rt_crystalforest-shumway ?= "463299bc2e533e1bd38b0053ae7b210980f269c3"

module_autoload_uio = "uio"
