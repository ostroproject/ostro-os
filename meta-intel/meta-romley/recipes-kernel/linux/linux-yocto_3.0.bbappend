FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_romley = "romley"
KMACHINE_romley  = "yocto/standard/common-pc-64/romley"

SRCREV_machine_pn-linux-yocto_romley ?= "fe3f155fa58db251640a5e110b861380b07b29f5"
SRCREV_meta_pn-linux-yocto_romley ?= "ae3e64c077972fe87f09946bd215620df68ca327"
