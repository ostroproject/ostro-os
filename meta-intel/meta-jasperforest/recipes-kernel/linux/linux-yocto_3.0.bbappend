FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_jasperforest = "jasperforest"

KMACHINE_jasperforest  = "yocto/standard/common-pc-64/jasperforest"

SRCREV_machine_pn-linux-yocto_jasperforest ?= "ca70dc1b835abd24ea1019b54169aab10a4a6f3b"
SRCREV_meta_pn-linux-yocto_jasperforest ?= "ae3e64c077972fe87f09946bd215620df68ca327"
